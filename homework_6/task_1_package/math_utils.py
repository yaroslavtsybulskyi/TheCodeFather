def factorial(n: int) -> int:
    """
    Function to calculate the factorial of an integer number.
    :param n: integer number to calculate the factorial of
    :return: integer number, factorial of n
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
    Function to find the greatest common denominator of a and b.
    :param a: integer number to find the greatest common denominator
    :param b: integer number to find the greatest common denominator
    :return: the greatest common denominator
    """
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError('a and b must be integers')
    a, b = abs(a), abs(b)
    if b == 0:
        return a
    while b != 0:
        a, b = b, a % b
    return a
