"""
Module: parallel_file_search
----------------------------
This module implements a parallel file search program that looks for a given
text across multiple large files concurrently using the `threading` module.
"""

import threading
import logging

from typing import List

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


def search_in_file(search_text: str, file_name: str) -> None:
    """
    Searches for a given text in a file and prints matching lines.
    :param search_text: The text to search for in the file.
    :param file_name: The name of the file to search in.
    :return: None
    :raises TypeError: If search_text is not a string.
    :raises TypeError: If file_name is not a string.
    :raises FileNotFoundError: If file_name does not exist.
    """
    if not isinstance(search_text, str):
        raise TypeError('search_text must be a string')
    if not isinstance(file_name, str):
        raise TypeError('file_name must be a string')

    try:
        match_count = 0
        search_text_lowercased = search_text.lower()

        with open(file_name, "r", encoding='utf-8') as file:
            lines = file.readlines()

            if not lines:
                logging.warning(f"{file_name} is empty")
                return

            for line_number, line in enumerate(lines, start=1):
                if search_text_lowercased in line.lower().strip():
                    logging.info(f"{search_text} found in {file_name}: line {line_number} ")
                    match_count += 1

            if match_count == 0:
                logging.info(f"No matches found for {search_text} in {file_name}")
            else:
                logging.info(f"Found {match_count} matches for {search_text} in {file_name}")
    except FileNotFoundError:
        logging.error(f"{file_name}: file not found")


def parallel_search(search_text: str, file_list: List[str]) -> None:
    """
    Searches for a given text across multiple files in parallel using threads.
    :param search_text: The text to search for.
    :param file_list: List of file paths to search in.
    :return: None
    """
    threads = []

    for file_name in file_list:
        thread = threading.Thread(target=search_in_file, args=(search_text, file_name))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()


if __name__ == "__main__":
    files = ['task_5_test/file_one.txt',
             'task_5_test/file_two.txt',
             'task_5_test/file_three.txt',
             'task_5_test/file_four.txt']

    parallel_search("Over fact all son tell this any his.", files)
