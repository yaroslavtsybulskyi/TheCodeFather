"""
main.py
=======

This script demonstrates the usage of mathematical and string utility functions
from the `math_utils` and `string_utils` modules.

Functions from `math_utils`:
- factorial: Calculates the factorial of a given integer.
- greater_common_denominator: Finds the greatest
common denominator of two integers.

Functions from `string_utils`:
- upper_register: Converts a string to uppercase.
- remove_spaces: Removes leading and trailing spaces from a string.
"""

from math_utils import factorial, greater_common_denominator
from string_utils import upper_register, remove_spaces

if __name__ == '__main__':
    print(factorial(6))
    print(greater_common_denominator(10, 5))
    print(upper_register("Hello World"))
    print(remove_spaces(" James Jameson "))
