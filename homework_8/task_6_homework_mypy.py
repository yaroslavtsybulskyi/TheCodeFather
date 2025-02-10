from typing import List, Tuple, Union, Callable, TypeVar

T = TypeVar("T")


def calculate_discount(price: float, discount: float) -> float:
    """
    Returns the price of the product after discounting.
    :param price: price of the product before discount.
    :param discount: percentage of the discount.
    :return: price of the product after discount.

    :raises ValueError: if price is less than 0.
    :raises ValueError: if discount is not a number.
    :raises TypeError: if price is not a number.
    :raises TypeError: if discount is not a number.
    """
    if not isinstance(price, (float, int)):
        raise TypeError("Price must be a float")
    if not isinstance(discount, (float, int)):
        raise TypeError("Discount percentage must be a float")
    if price <= 0:
        raise ValueError("Price must be bigger than 0")
    if discount < 0:
        raise ValueError("Discount must be bigger than 0")
    if discount >= 100:
        return 0
    return round(price * (1 - discount / 100), 2)


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
