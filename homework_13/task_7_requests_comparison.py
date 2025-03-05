"""
Module: performance_comparison
-------------------------------
This module compares the performance of different approaches for executing multiple HTTP requests:
1. Synchronous (one request at a time)
2. Multithreading (ThreadPoolExecutor)
3. Multiprocessing (ProcessPoolExecutor)
4. Asynchronous (aiohttp + asyncio)
"""

import asyncio
import concurrent.futures
import functools
import ssl
import time

import aiohttp
import certifi
import requests

URL: str = "https://httpbin.org/"
NUMBER_OF_REQUESTS: int = 50
ssl_context = ssl.create_default_context(cafile=certifi.where())


def measure_time(func):
    """
    Decorator to measure execution time of synchronous and asynchronous functions.
    :param func: Function to be measured.
    :return: Wrapped function with timing functionality.
    """
    if asyncio.iscoroutinefunction(func):  # Check if function is async
        @functools.wraps(func)
        async def async_wrapper(*args, **kwargs):
            start_time = time.time()
            result = await func(*args, **kwargs)  # Await async function
            end_time = time.time()
            print(f"[{func.__name__.upper()}] Completed in {end_time - start_time:.2f} seconds")
            return result

        return async_wrapper
    else:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            print(f"[{func.__name__.upper()}] completed in {end_time - start_time:.2f} seconds")
            return result

        return wrapper


@measure_time
def run_synchronously() -> None:
    """
    Runs HTTP requests sequentially (one at a time).
    :return: None
    """
    for i in range(NUMBER_OF_REQUESTS):
        requests.get(URL)


@measure_time
def run_multithreads(max_threads: int = 5) -> None:
    """
    Runs HTTP requests using multithreading.
    :param max_threads: Number of concurrent threads. Defaults to 5.
    :return: None
    :raises TypeError: If max_threads is not an integer.
    """
    if not isinstance(max_threads, int):
        raise TypeError("max_threads must be an integer.")
    with concurrent.futures.ThreadPoolExecutor(max_threads) as executor:
        futures = [executor.submit(requests.get, URL) for i in range(NUMBER_OF_REQUESTS)]
        concurrent.futures.wait(futures)


@measure_time
def run_multiprocessing(max_processes: int = 5) -> None:
    """
    Runs HTTP requests using multiprocessing.
    :param max_processes: Number of concurrent processes.
    :return: None
    :raises TypeError: If max_processes is not an integer.
    """
    if not isinstance(max_processes, int):
        raise TypeError("max_processes must be an integer.")

    with concurrent.futures.ProcessPoolExecutor(max_processes) as executor:
        futures = [executor.submit(requests.get, URL) for i in range(NUMBER_OF_REQUESTS)]
        concurrent.futures.wait(futures)


@measure_time
async def run_asynchronously() -> None:
    """
    Runs HTTP requests asynchronously using aiohttp.
    """

    async def fetch(session: aiohttp.ClientSession, url: str) -> None:
        """
        Sends an asynchronous GET request to a given URL and reads the response.
        :param session: An active aiohttp ClientSession used for making requests.
        :param url: The URL to send the request to.
        :return: None
        :raises TypeError: If session is not an instance of aiohttp.ClientSession.
        :raises TypeError: If url is not an instance of URL.
        """
        if not isinstance(session, aiohttp.ClientSession):
            raise TypeError("session must be an instance of aiohttp.ClientSession.")
        if not isinstance(url, str):
            raise TypeError("url must be an instance of str.")

        async with session.get(url) as response:
            await response.read()
            return

    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=ssl_context)) as session:
        tasks = [fetch(session, URL) for _ in range(NUMBER_OF_REQUESTS)]
        await asyncio.gather(*tasks)


if __name__ == '__main__':
    run_synchronously()
    run_multithreads()
    run_multiprocessing()
    asyncio.run(run_asynchronously())
