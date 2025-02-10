"""
Apply function module
This module provides functions to apply mathematical operations to numbers.
It includes:
    - `square(number)`: Returns the square of a number.
    - `double(number)`: Returns the double of a number.
    - `apply_operation(number, func)`: Applies a given function to a number.
"""

from typing import Callable


def square(number: int) -> int:
    """
    Returns the square of a number.
    :param number: number to square
    :return: square of number
    :raises TypeError: if number is not an integer
    """
    if not isinstance(number, int):
        raise TypeError('number must be an integer')
    return number ** 2


def double(number: int) -> int:
    """
    Returns the double of a number.
    :param number: number to double
    :return: doubled number
    :raises TypeError: if number is not an integer
    """
    if not isinstance(number, int):
        raise TypeError('number must be an integer')
    return number * 2


def apply_operation(number: int, func: Callable[[int], int]) -> int:
    """
    Functions that applies another function to a number.
    :param number: number to use
    :param func: function to apply
    :return: result of applying func to number
    :raises TypeError: if number is not an integer
    """
    if not isinstance(number, int):
        raise TypeError('number must be an integer')
    return func(number)


if __name__ == '__main__':
    print(apply_operation(5, square))
    print(apply_operation(5, double))
