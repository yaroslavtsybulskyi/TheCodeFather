"""
string_utils.py
===============

This module provides utility functions for manipulating strings:
- Converting a string to uppercase.
- Removing leading and trailing spaces from a string.
"""


def upper_register(text: str) -> str:
    """
    Converts the given string to uppercase.
    This function takes a string and returns the same string in uppercase letters.
    :param text: The string to be converted to uppercase.
    :type text: str
    :return: The converted string in uppercase.
    :rtype: str
    :raises TypeError: If text is not a string.
    """
    return text.upper()


def remove_spaces(text: str) -> str:
    """
    Removes leading and trailing spaces from the given string.
    This function trims the whitespace at the beginning and end of the string.
    :param text: The string to be checked for spaces.
    :type text: str
    :return: The string with spaces removed from both ends.
    :rtype: str
    :raises TypeError: If text is not a string.
    """
    return text.strip()
