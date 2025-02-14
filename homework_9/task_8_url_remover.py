"""
URL remover module
This module provides a function `url_remover` to remove all urls in the text.
"""

import re


def url_remover(text: str) -> str:
    """
    Remove all urls in the text.
    :param text: text to be processed
    :return: text with all urls removed
    :raises TypeError: if text is not a string
    """
    if not isinstance(text, str):
        raise TypeError('Text must be a string')

    url_pattern = re.compile(r'https?://[^\s]+|www\.[^\s]+')

    return re.sub(url_pattern, '', text)


if __name__ == '__main__':
    print(url_remover("Visit https://example.com for details."))
    print(url_remover('No URLs here!'))
    print(url_remover('Links: https://one.com and www.two.com'))
