"""
Asynchronous Fetcher Module
"""

import asyncio
from typing import Dict, Any, Awaitable


class AsyncFetcher:
    """
    A simple asynchronous fetcher that simulates fetching data from a URL.
    """

    async def fetch(self, url: str) -> [Dict[str, Any]]:
        """
        Simulates fetching data asynchronously.

        :param url: The URL to fetch data from.
        :return: A dictionary containing the response data.
        """
        print(f"Loading {url}...")

        await asyncio.sleep(1)

        return {'page': url, 'status_code': 200, 'data': {'message': 'OK'}, }


async def main():
    """
    Runs the asynchronous fetcher and prints the fetched result.
    """
    fetcher = AsyncFetcher()
    result = await fetcher.fetch("https://example.com/api")
    print(result)


if __name__ == "__main__":
    asyncio.run(main())
