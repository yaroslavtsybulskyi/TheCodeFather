"""
Input Parsing Module
This module provides a function `parse_input` to handle different input types.
"""

from typing import Union


def parse_input(data: Union[int, str]) -> Union[int, None]:
    """
    Parses an input (integer or string) and converts it to an integer.
    :param data: input value which can be integer or string
    :return: output value: integer or None
    :raises ValueError: if the input is string not convertible to integer
    :raises TypeError: if the input is other data type that int or string
    """
    if isinstance(data, int):
        return data
    elif isinstance(data, str):
        try:
            return int(data)
        except ValueError:
            return None
    else:
        raise TypeError("Expected input: int or str")


if __name__ == "__main__":
    print(parse_input(42))  # 42
    print(parse_input("100"))  # 100
    print(parse_input("hello"))  # None
