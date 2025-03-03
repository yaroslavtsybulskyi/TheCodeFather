"""
Module: async_url_downloader
----------------------------
This module provides functionality to asynchronously simulate downloading
web pages using `asyncio`. Each page download is simulated with a random
delay between 1 and 5 seconds.
"""

import asyncio
import random
from typing import List


async def download_page(url: str) -> None:
    """
    Simulates downloading a web page asynchronously.
    :param url: The URL of the page to download.
    :return: None
    """
    delay = random.randint(1, 5)
    await asyncio.sleep(delay)
    print(f"{url} was downloaded in {delay} seconds")


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
