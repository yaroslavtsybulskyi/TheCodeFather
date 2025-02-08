"""
Math Utility Functions

This module provides utility functions for basic mathematical operations,
including checking if a number is even and calculating the factorial of a number.
"""


def is_even(n: int) -> bool:
    """
    Checks if n is even.

    :param n: Integer to check.
    :return: True if n is even, False otherwise.

    >>> is_even(2)
    True
    >>> is_even(3)
    False
    """
    return n % 2 == 0


def factorial(n: int) -> int:
    """
    Returns the factorial of n.
    :param n: number
    :return: Factorial of n

    >>> factorial(0)
    1
    >>> factorial(1)
    1
    >>> factorial(5)
    120
    >>> factorial(-5)
    Traceback (most recent call last):
        ...
    ValueError: n must be positive
    """
    if not isinstance(n, int):
        raise TypeError('n must be an integer')
    if n < 0:
        raise ValueError('n must be positive')
    if n == 0:
        return 1
    return n * factorial(n - 1)
