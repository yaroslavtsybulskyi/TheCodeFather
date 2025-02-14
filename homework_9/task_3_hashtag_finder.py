"""
Hashtag Finder Module
This module provides a function `hashtag_finder` to find hashtags in the text.
"""

import re

from typing import List


def hashtag_finder(text: str) -> List[str]:
    """
    Hashtag Finder Function
    :param text: text to be processed
    :return: list of hashtags
    :raises TypeError: if text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError('text must be a string')

    hashtag_pattern = re.compile(r'#\w+')

    return re.findall(hashtag_pattern, text)


if __name__ == '__main__':
    test_text = "No hashtags here, just some text."
    test_hashtags = "Exploring the mountains today! #1 #Adventure #NatureLover #Hiking"

    print(hashtag_finder(test_text))
    print(hashtag_finder(test_hashtags))
