"""
Module: file_downloader
------------------------
This module provides functionality to download files from the internet efficiently.
It supports downloading multiple files in parallel using ThreadPoolExecutor,
limits concurrency to prevent system overload, and includes error handling for
network failures and file system issues.
"""

import mimetypes
import os
import logging
import uuid
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from typing import List
from urllib.parse import urlparse

import requests

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

DOWNLOAD_DIR = Path('downloads')
DOWNLOAD_DIR.mkdir(parents=True, exist_ok=True)


def generate_filename(url: str, response: requests.Response) -> str:
    """
    Generates a filename based on the URL or HTTP response headers.
    If the URL does not contain a valid filename, a unique UUID-based name is generated.
    If the file extension is missing, it is extracted from the Content-Type header.
    :param url: The URL of the file.
    :param response: The HTTP response object from requests.
    :return: A valid filename with an appropriate extension.
    :raises TypeError: If response is not a requests.Response object.
    """
    if not isinstance(response, requests.Response):
        raise TypeError('Response is not an instance of requests.Response')
    parsed_url = urlparse(url)
    path = parsed_url.path
    filename = os.path.basename(path)

    if not filename or '?' in filename:
        filename = str(uuid.uuid4())

        content_type = response.headers.get('content-type')
        extension = mimetypes.guess_extension(content_type) if content_type else None

        filename += extension

    return filename


def download_file(url: str) -> None:
    """
    Downloads a file from the given URL and saves it locally.
    :param url: The URL of the file to download.
    :returns: None
    :raises TypeError: If `url` is not a string.
    :raises requests.exceptions.RequestException: If a network error occurs.
    :raises OSError: If an error occurs while writing to the file.
    """
    if not isinstance(url, str):
        raise TypeError('url must be a string')

    try:
        response = requests.get(url, stream=True, timeout=10)
        response.raise_for_status()

        filename = generate_filename(url, response)
        file_path = DOWNLOAD_DIR / filename

        total_size = int(response.headers.get('content-length', 0))
        downloaded = 0
        try:
            with open(file_path, 'wb') as file:
                for chunk in response.iter_content(chunk_size=1024):
                    if chunk:
                        file.write(chunk)
                        downloaded += len(chunk)
                        if total_size:
                            progress = (downloaded / total_size) * 100
                            print(f'Downloaded {progress:.2f}% of {filename}')

                logging.info(f'{filename} successfully downloaded')
                return
        except OSError as e:
            logging.error(f'Error creating {filename}: {e}')

    except requests.exceptions.RequestException as e:
        logging.error(f"Download error: {e} - {url} ")


def parallel_downloader(urls: List[str], max_workers: int = 5) -> None:
    """
    Downloads multiple files in parallel using ThreadPoolExecutor.
    Limits the number of concurrent downloads to prevent system overload.
    :param urls: A list of URLs to download.
    :param max_workers: The maximum number of simultaneous downloads.
    :return: None
    :raises TypeError: If `urls` is not a list or `max_workers` is not an integer.
    """
    if not isinstance(urls, list):
        raise TypeError('urls must be a list')
    if not isinstance(max_workers, int):
        raise TypeError('max_workers must be a integer')

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        future_to_url = {executor.submit(download_file, url): url for url in urls}

        for future in as_completed(future_to_url):
            try:
                future.result()
            except Exception as e:
                logging.error(f'An error occurred: {e}')


if __name__ == '__main__':
    urls = ['https://thepublicdomain.org/thepublicdomain1.pdf',
            'https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf',
            'https://www.sldttc.org/allpdf/21583473018.pdf']

    parallel_downloader(urls, max_workers=3)
