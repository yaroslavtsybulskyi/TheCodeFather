"""
IP address finder module
This module provides a function `ip_address_finder` to find ip addresses in the text.
"""

import re

from typing import List


def ip_address_finder(text: str) -> List[str]:
    """
    Finds ip addresses in a text string.
    :param text: text to be parsed.
    :return: list of ip addresses.
    :raises TypeError: if `text` is not a string.
    """
    if not isinstance(text, str):
        raise TypeError('text must be a string')

    ip_address_pattern = re.compile(r'\b(?:25[0-5]|2[0-4][0-9]|[0-1]?[0-9]'
                                    r'[0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.'
                                    r'(?:25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.(?:25'
                                    r'[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\b')
    return re.findall(ip_address_pattern, text)


if __name__ == '__main__':
    text_1 = '192.168.127.12 is an IP address, but 999.999.999.999 is not'
    text_2 = "Server IP: 192.168.1.1, Backup IP: 10.0.0.255"
    print(ip_address_finder(text_1))
    print(ip_address_finder(text_2))
