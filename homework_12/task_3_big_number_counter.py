"""
Module: parallel_sum_calculator
-------------------------------
This module provides functionality to compute the sum of a large list in parallel
using Python's `multiprocessing` module. It efficiently divides the list into chunks
and processes them using multiple CPU cores.
"""

import multiprocessing as mp
import random
from typing import Union, List

import numpy as np


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
    :return: Number of processes to use. Defaults to 4.
    :raises TypeError: If numbersList was not a list.
    :raises TypeError: If number_of_processes was not a int.
    :raises TypeError: If numbers inside the list are not a float or an integer.
    """
    if not isinstance(numbers_list, list):
        raise TypeError("numbersList must be a list")

    if all(not isinstance(int, float) for number in numbers_list):
        raise TypeError("Data should be a integer or float")

    if not isinstance(number_of_processes, int):
        raise TypeError("Number of processes must be a integer")

    try:
        chunks = np.array_split(numbers_list, number_of_processes)

        with mp.Pool(number_of_processes) as pool:
            temp_result = pool.map(chunk_sum, chunks)
    except Exception as e:
        print(f"Error: {e}")

    return sum(temp_result)


if __name__ == '__main__':
    numbers = [random.randint(1, 100) for _ in range(1000000)]
    total = multi_sum(numbers)
    print(f"Result: {total}")

    float_numbers = [random.uniform(1.00, 100.00) for _ in range(1000000)]
    total = multi_sum(float_numbers)
    print(f"Result: {total}")
