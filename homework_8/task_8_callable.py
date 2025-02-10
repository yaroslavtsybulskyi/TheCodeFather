"""
Processor Module

This module provides a generic class `Processor[T]` that allows applying a transformation
function to a list of elements.
"""

from typing import List, TypeVar, Callable

T = TypeVar('T')


class Processor:
    """
    A generic processor class that applies a function to each element of a list.
    """

    def __init__(self, data: List[T]) -> None:
        """
        Constructor.
        :param data: A list of elements of type T.
        """
        self.data = data

    def apply(self, func: Callable[[T], T]) -> List[T]:
        """
        Applies the function to the list of elements.
        :param func: function to apply to each element.
        :return: the list of elements of type T after applying the function.
        """
        return [func(item) for item in self.data]


def double(number: int) -> int:
    """
    Simple function that doubles the given number.
    :param number: number to double.
    :return: result of doubling the given number.
    """
    return number * 2


def to_upper(string: str) -> str:
    """
    Converts a string to uppercase.
    :param string: string to convert.
    :return: result of converting to uppercase.
    """
    return string.upper()


if __name__ == '__main__':
    p1 = Processor([1, 2, 3])
    print(p1.apply(lambda x: x * 2))
    print(p1.apply(double))

    p2 = Processor(["hello", "world"])
    print(p2.apply(str.upper))
    print(p2.apply(to_upper))
