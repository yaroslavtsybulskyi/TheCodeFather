"""
Module: file_downloader
------------------------
This module provides functionality to download files from the internet efficiently.
It supports downloading multiple files in parallel using multithreading.
"""

import threading
from typing import List

import requests


def download_file(url: str) -> None:
    """
    Downloads a file from the given URL and saves it locally.
    :param url: The URL of the file to download.
    :returns: None
    :raises TypeError: If `url` is not a string.
    :raises RequestException: In case of error during download.
    """
    if not isinstance(url, str):
        raise TypeError('url must be a string')

    try:
        filename = url.split('/')[-1]

        response = requests.get(url, stream=True)
        response.raise_for_status()

        with open(filename, 'wb') as file:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    file.write(chunk)

            print(f'{filename} successfully downloaded')
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")


def parallel_downloader(urls: List[str]) -> None:
    """
    Downloads multiple files in parallel using threading.
    :param urls: The list of the URLs of the files to download.
    :return: None
    :raises TypeError: If `urls` is not a list.
    """
    if not isinstance(urls, list):
        raise TypeError('urls must be a list')

    threads = []

    for url in urls:
        thread = threading.Thread(target=download_file, args=(url,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()


if __name__ == '__main__':
    urls = ['https://thepublicdomain.org/thepublicdomain1.pdf',
            'https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf',
            'https://www.sldttc.org/allpdf/21583473018.pdf']

    parallel_downloader(urls)
