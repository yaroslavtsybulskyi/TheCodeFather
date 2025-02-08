"""
StringProcessor Module

This module provides utility functions for string manipulation:
- Reversing strings
- Capitalizing the first letter
- Counting vowels in a string
"""


class StringProcessor:
    """
    Class for string processing
    """

    @staticmethod
    def reverse_string(s: str) -> str:
        """
        Method for reversing strings
        :param s: string to be reversed
        :return: reversed string
        """
        if not isinstance(s, str):
            raise TypeError('Input must be a string')
        return s[::-1]

    @staticmethod
    def capitalize_string(s: str) -> str:
        """
        Method for capitalizing strings
        :param s: string for processing
        :return: capitalized string
        """
        if not isinstance(s, str):
            raise TypeError('Input must be a string')
        return s.capitalize()

    @staticmethod
    def count_vowels(s: str) -> int:
        """
        Method for counting vowels in the string that is passed as parameter
        :param s: string to be checked
        :return: number of vowels
        """
        if not isinstance(s, str):
            raise TypeError('Input must be a string')
        vowels = 'aeiou'
        return sum(1 for char in s.lower() if char in vowels)
