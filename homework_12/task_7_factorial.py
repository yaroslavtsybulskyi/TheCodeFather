"""
Module: factorial_calculation
----------------------------
This module provides functionality to compute the factorial of a number
efficiently using multiprocessing. It divides the computation into chunks
and processes them in parallel.
"""

import multiprocessing
import math
import logging


def partial_factorial(start: int, end: int) -> int:
    """
    Computes the product of integers in the given range [start, end].
    :param start: The starting integer of the range.
    :param end: The ending integer of the range.
    :return: The factorial product of numbers in the range.
    """
    result = 1
    for i in range(start, end + 1):
        result *= i
    return result


def parallel_factorial(number: int, number_of_processes: int = 4) -> int:
    """
    Computes the factorial of a number using multiple processes.
    :param number: The number whose factorial is to be computed.
    :param number_of_processes: The number of parallel processes to use (default is 4).
    :return: The factorial of the given number.
    :raises TypeError: If `number` or `number_of_processes` is not an integer.
    :raises ValueError: If `number` is negative or `number_of_processes` is less than 1.
    """
    if not isinstance(number, int) or not isinstance(number_of_processes, int):
        raise TypeError("Both 'number' and 'number_of_processes' must be integers.")

    if number < 0:
        raise ValueError("Number cannot be negative")
    if number_of_processes < 1:
        raise ValueError("Number of processes cannot be less than 1")

    if number == 0 or number == 1:
        return 1
    try:
        step = number // number_of_processes
        pool = multiprocessing.Pool(processes=number_of_processes)
        tasks = [(i * step + 1, (i + 1) * step if i != number_of_processes - 1 else number)
                 for i in range(number_of_processes)]
        results = pool.starmap(partial_factorial, tasks)
        pool.close()
        pool.join()
        return math.prod(results)
    except Exception as e:
        logging.error("Error: %s", e)
        return 0


if __name__ == "__main__":
    print(parallel_factorial(50))
