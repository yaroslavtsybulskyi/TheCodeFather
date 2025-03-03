"""
Module: parallel_sum_calculator
-------------------------------
This module provides functionality to compute the sum of a large list in parallel
using Python's `multiprocessing` module. It efficiently divides the list into chunks
and processes them using multiple CPU cores.
"""

import multiprocessing as mp
import random
import logging
from typing import Union, List

import numpy as np

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


def chunk_sum(chunk: List[Union[int, float]]) -> Union[int, float]:
    """
    Computes the sum of a chunk of numbers.
    :param chunk: A list of integers or floats.
    :return: The sum of the chunk.
    """
    return sum(chunk)


def multi_sum(numbers_list: List[Union[int, float]], number_of_processes: int = 4) \
        -> Union[int, float]:
    """
    Computes the sum of a list in parallel using multiprocessing.
    :param numbers_list: The list of numbers to calculate sum of.
    :param number_of_processes: Number of processes to use. Defaults to 4.
    :return: The sum of the numbers in numbers_list.
    :raises TypeError: If numbersList was not a list.
    :raises TypeError: If number_of_processes was not an int.
    :raises TypeError: If numbers inside the list are not a float or an integer.
    """
    if not isinstance(numbers_list, list):
        raise TypeError("numbersList must be a list")

    if not all(isinstance(number, (int, float)) for number in numbers_list):
        raise TypeError("All elements in numbers_list must be integers or floats")

    if not isinstance(number_of_processes, int):
        raise TypeError("Number of processes must be a integer")

    try:
        chunks = np.array_split(numbers_list, number_of_processes)

        with mp.Pool(number_of_processes) as pool:
            temp_result = pool.map(chunk_sum, chunks)
    except Exception as e:
        logging.error("Multiprocessing error: %s", e)
        return None

    return sum(temp_result)


if __name__ == '__main__':
    numbers = [random.randint(1, 100) for _ in range(1000000)]
    total = multi_sum(numbers)
    print(f"Result: {total}")

    float_numbers = [random.uniform(1.00, 100.00) for _ in range(1000000)]
    total = multi_sum(float_numbers)
    print(f"Result: {total}")
