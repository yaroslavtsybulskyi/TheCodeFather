"""
Password strength checker module
This module provides a function `password_checker` to check if password is strong.
"""

import re


def password_checker(password: str) -> bool:
    """
    Checks if password is strong
    :param password: password to check
    :return: bool value indicating if password is strong
    :raises TypeError: if password is not string.
    """
    if not isinstance(password, str):
        raise TypeError('Password must be a string')

    password_pattern = re.compile(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@#$%^&+=!]).{8,}$")
    return bool(re.fullmatch(password_pattern, password))


if __name__ == '__main__':
    print(password_checker('<PASSWORD>'))
    print(password_checker('1aA55@'))
    print(password_checker('1aA55@43dd'))
    print(password_checker('1aA55@4'))
