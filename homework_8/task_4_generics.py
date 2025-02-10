"""
Getting first element module
This module provides a function that returns the first element and
none if there is no elements in the list
"""

from typing import List, TypeVar, Union

T = TypeVar('T')


def get_first(my_list: List[T]) -> Union[T, None]:
    """
    Returns the first element of a given list or None if the list is empty.
    :param my_list: A list of any type.
    :return: The first element of the list, or None if the list is empty.
    :raises TypeError: If the argument is not a list.
    """
    if not isinstance(my_list, list):
        raise TypeError('Please, enter list as an argument.')
    return my_list[0] if my_list else None


if __name__ == '__main__':
    print(get_first([1, 2, 3]))  # 1
    print(get_first(["a", "b", "c"]))  # "a"
    print(get_first([]))  # None
