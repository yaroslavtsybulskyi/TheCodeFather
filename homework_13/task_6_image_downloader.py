"""
Module: async_image_downloader
------------------------------
This module provides an asynchronous image downloader using `aiohttp`.
"""

import aiohttp
import asyncio
import logging
import ssl

from pathlib import Path
from typing import List, Tuple

import aiofiles
import certifi

logging.basicConfig(level=logging.INFO)

ssl_context = ssl.create_default_context(cafile=certifi.where())

DOWNLOAD_DIR = Path("images")
DOWNLOAD_DIR.mkdir(parents=True, exist_ok=True)


async def download_image(image_url: str, image_name: str) -> None:
    """
    Downloads an image asynchronously and saves it to a file.

    :param image_url: The URL of the image to download.
    :param image_name: The name of the file to save the image as.
    :return: None
    :raises TypeError: If image_url or image_name is not a string.
    :raises aiohttp.ClientError: If the HTTP request fails.
    :raises OSError: If there is an issue saving the file.
    """
    if not isinstance(image_url, str) or not isinstance(image_name, str):
        raise TypeError("Image url and image name must be strings.")

    try:
        async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=ssl_context)) as session:
            async with session.get(image_url) as response:
                if response.status != 200:
                    logging.error("Response Status: %s.Error downloading image: %s",
                                  response.status, image_name)
                    return

                file_path = DOWNLOAD_DIR / image_name

                async with aiofiles.open(file_path, "wb") as file:
                    await file.write(await response.read())

                logging.info("Downloaded image: %s", image_name)
    except aiohttp.ClientError as e:
        logging.error("HTTP request failed for %s: %s", image_url, e)
    except OSError as e:
        logging.error("File save error for %s: %s", image_name, e)
    except Exception as e:
        logging.error("Unexpected error occurred while downloading %s: %s", image_url, e)


async def main(image_list: List[Tuple[str, str]]) -> None:
    """
    Downloads multiple images concurrently.

    :param image_list: A list of tuples (image_url, filename).
    :return: None
    :raises ValueError: If the input list is not list of tuples of 2 elements.
    :raises TypeError: If image_list is not a list.
    """
    if not isinstance(image_list, list):
        raise TypeError("Image list must be a list")
    if not all(isinstance(i, tuple) and len(i) == 2 for i in image_list):
        raise ValueError("Each item in image_list must be a tuple of (url, filename).")

    tasks = [download_image(image_url, image_name) for image_url, image_name in image_list]
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    image_list = [("https://www.churchpop.com/content/images/size/w1200/wordpress/2017/01/111.jpg", "Homer.jpg"),
                  ("https://sketchok.com/images/articles/01-cartoons/001-simpsons/03/12.jpg", "Moe.jpg"),
                  ("https://upload.wikimedia.org/wikipedia/en/d/de/Barney_Gumble.png", "Barney.png")]

    asyncio.run(main(image_list))
