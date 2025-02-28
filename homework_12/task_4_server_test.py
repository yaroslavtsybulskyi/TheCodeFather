"""
Module: multi_threaded_http_client
----------------------------------
This module implements a multi-threaded HTTP client that sends multiple
requests to a web server concurrently using Python's `threading` module.
"""

import threading
import time
import requests


def send_request(thread_id: int) -> None:
    """
    Sends an HTTP GET request to the server.
    :param thread_id: id of the thread being requested.
    :return: None
    :raises TypeError: if `thread_id` is not an int.
    """
    if not isinstance(thread_id, int):
        raise TypeError("thread_id must be an integer")

    url = "http://localhost:8080"

    try:
        response = requests.get(url)
        print(f"Thread {thread_id}: {response.text}")
    except Exception as e:
        print(f"Error: {e}")

    time.sleep(2)


def send_multiple_request(number_of_requests: int = 5) -> None:
    """
    Sends multiple HTTP GET requests concurrently using threads.
    :param number_of_requests: Number of requests to send. Default is 5.
    :return: None
    :raises TypeError: if `number_of_requests` is not an int.
    """
    if not isinstance(number_of_requests, int):
        raise TypeError("number_of_requests must be an integer")
    threads = []

    try:
        for i in range(number_of_requests):
            thread = threading.Thread(target=send_request, args=(i,))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    send_multiple_request(6)
