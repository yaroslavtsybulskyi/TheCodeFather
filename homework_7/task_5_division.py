"""
Math Utility Module

This module provides mathematical functions, including a safe division function.

Functions:
    - divide(a, b): Divides two numbers with error handling for division by zero.
"""


def divide(a: int, b: int) -> float:
    """
    Divides two numbers with error handling for division by zero.
    :param a: The numerator.
    :param b: The denominator.
    :return: The division result as a float.

    :raises ZeroDivisionError: If `b` is zero.
    :raises TypeError: If `a` or `b` is not a number.
    """
    if not isinstance(a, int):
        raise TypeError('Argument must be a number.')
    if not isinstance(b, int):
        raise TypeError('Argument must be a number.')
    if b == 0:
        raise ZeroDivisionError('Cannot divide by zero.')
    return a / b
