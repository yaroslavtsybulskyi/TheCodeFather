"""
Filter Adults Module
This module provides a function `filter_adults` to filter out individuals who are 18 years or older
from a given list of people with names and ages.
"""

from typing import List, Tuple


def filter_adults(people: List[Tuple[str, int]]) -> List[Tuple[str, int]]:
    """
    Function returns persons who are adults.
    :param people: list of people tuples
    :return: list of people who are adults
    :raises TypeError: if people parameter is not a list
    """
    if not isinstance(people, list):
        raise TypeError('People must be a list')
    return [(name, age) for (name, age) in people if age >= 18]


if __name__ == '__main__':
    people = [("Andrew", 25), ("Kate", 16), ("Mary", 19), ("Jim", 15)]
    print(filter_adults(people))
