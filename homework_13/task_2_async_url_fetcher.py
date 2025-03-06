"""
Module: async_http_fetcher
--------------------------
This module provides functionality to asynchronously fetch the content
of multiple web pages using `aiohttp` and `asyncio`.
"""

import asyncio
import aiohttp
import logging

from typing import List

logging.basicConfig(level=logging.INFO)


async def fetch_content(url: str) -> str:
    """
    Asynchronously fetches the content of a web page.
    :param url: The URL of the page to fetch.
    :return: The HTML content of the page as a string or an error message.
    :raises TypeError: If `url` is not a string.
    """
    if not isinstance(url, str):
        raise TypeError('url must be a string')

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, timeout=10) as response:
                response.raise_for_status()
                return await response.text()
    except aiohttp.ClientError as e:
        logging.error("Error while fetching %s: %s", url, e)
        return f"Request failed for {url}: {e}"
    except asyncio.TimeoutError as e:
        logging.error("Timeout error while fetching %s: %s", url, e)
        return f"Request timed out for {url}: {e}"
    except Exception as e:
        logging.error("Unexpected error while fetching %s: %s", url, e)
        return f"Unexpected error for {url}: {e}"


async def fetch_all(url_list: List[str]) -> List[str]:
    """
    Asynchronously fetches multiple web pages concurrently.
    :param url_list: A list of URLs to fetch.
    :return: A list of HTML content or error messages.
    :raises TypeError: If `url_list` is not a list of strings.
    """
    if not isinstance(url_list, list) or not all(isinstance(url, str) for url in url_list):
        raise TypeError('url_list must be a list of strings')

    tasks = [fetch_content(url) for url in url_list]
    return await asyncio.gather(*tasks)


if __name__ == '__main__':
    url_list = ['https://www.google.com', 'https://yahoo.com',
                'https://ukr.net']

    result = asyncio.run(fetch_all(url_list))

    for url, result in zip(url_list, result):
        print(url, result)
