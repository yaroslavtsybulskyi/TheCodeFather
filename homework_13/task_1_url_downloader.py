"""
Module: async_url_downloader
----------------------------
This module provides functionality to asynchronously simulate downloading
web pages using `asyncio` and `aiohttp`.
"""

import asyncio
import logging
from typing import List
import aiohttp

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


async def download_page(url: str) -> str:
    """
    Asynchronously download a web page.
    :param url: The URL of the page to download.
    :return: The content of the page if successful, otherwise an error message.

    :raises TypeError: If `url` is not a string.
    """
    if not isinstance(url, str):
        raise TypeError("URL must be a string.")

    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(url, timeout=10) as response:
                response.raise_for_status()
                content = await response.text()
                logging.info("%s has been successfully downloaded.", url)
                return content
        except aiohttp.ClientError as e:
            logging.error("Error while downloading %s: %s", url, e)
            return f"Error while downloading {url}: {e}"
        except asyncio.TimeoutError as e:
            logging.error("Timeout error while downloading %s: %s", url, e)
            return f"Timeout error while downloading {url}: {e}"
        except Exception as e:
            logging.error("Unexpected error while downloading %s: %s", url, e)
            return f"Unexpected error while downloading {url}: {e}"


async def main(urls: List[str]):
    """
    Downloads multiple web pages concurrently using asyncio.
    :param urls: A list of URLs to be downloaded.
    :return: None
    """
    tasks = [download_page(url) for url in urls]
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    url_list = ['https://google.com', 'https://yahoo.com',
                'https://amazon.com', 'https://facebook.com']
    asyncio.run(main(url_list))
