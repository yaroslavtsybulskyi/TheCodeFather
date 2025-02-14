"""
Phone Number Finder Module
This module provides a function `phone_number_finder` to find phone numbers in the text.
"""

import re

from typing import List


def phone_number_finder(text: str) -> List[str]:
    """
    Finds phone numbers in the text.
    :param text: text to be processed
    :return: list of phone numbers found in the text
    :raises TypeError: if text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string.")

    phone_pattern = re.compile(r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}')

    return re.findall(phone_pattern, text)


if __name__ == "__main__":
    test_text = """Call me at (123) 456-7890 or 123-456-7890.
                You can also try 123.456.7890 or 1234567890.
                Avoid incorrect numbers like 123-45-7890 or (123)-4567-890."""

    print(phone_number_finder(test_text))
