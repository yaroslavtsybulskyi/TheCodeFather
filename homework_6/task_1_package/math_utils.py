"""
math_utils.py
==============

This module provides mathematical utility functions such as:
- Calculating the factorial of a number
- Finding the greatest common denominator of two numbers
"""


def factorial(n: int) -> int:
    """
    Function to calculate the factorial of an integer number.
    The factorial of a number n (denoted as n!) is the product of all
    positive integers less than or equal to n.
    Factorial is defined as: n! = n * (n-1) * (n-2) * ... * 1.
    Special case: 0! = 1.
    :param n: An integer number to calculate the factorial of.
    :type n: int
    :return: The factorial of n as an integer.
    :rtype: int
    :raises TypeError: If n is not an integer.
    :raises ValueError: If n is a negative integer.
    """
    if not isinstance(n, int):
        raise TypeError('n must be an integer')
    if n < 0:
        raise ValueError('n must be positive')
    if n == 0:
        return 1
    return n * factorial(n - 1)


def greater_common_denominator(a: int, b: int) -> int:
    """
    Function to find the greatest common denominator (GCD) of two integers, a and b.
    The greatest common denominator (also known as the greatest
    common divisor, or GCD) is the largest number
    that divides both a and b without leaving a remainder.
    This function uses the Euclidean algorithm to compute
    the GCD.
    :param a: The first integer to find the greatest common denominator.
    :type a: int
    :param b: The second integer to find the greatest common denominator.
    :type b: int
    :return: The greatest common denominator (GCD) of a and b.
    :rtype: int
    :raises TypeError: If a or b is not an integer.
    """
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError('a and b must be integers')
    a, b = abs(a), abs(b)
    if b == 0:
        return a
    while b != 0:
        a, b = b, a % b
    return a
