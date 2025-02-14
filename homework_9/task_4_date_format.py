"""
Date format module
This module provides a function `date_format` to convert from DD/MM/YYYY to YYYY-MM-DD
"""

import re


def date_format(date: str) -> str:
    """
    Convert date format from DD/MM/YYYY to YYYY-MM-DD
    :param date: date in format DD/MM/YYYY
    :return: date in format YYYY-MM-DD
    :raises: TypeError if date is not a string
    """
    if not isinstance(date, str):
        raise TypeError('Date must be a string')

    pattern = r'^(\d{1,2})/(\d{1,2})/(\d{4})$'
    match = re.fullmatch(pattern, date)
    if match:
        day, month, year = match.groups()
        return f'{year}/{month.zfill(2)}/{day.zfill(2)}'
    return f'{date} is in incorrect format. Use YYYY/MM/DD format'


if __name__ == '__main__':
    print(date_format('12/10/2020'))
    print(date_format('1/6/2022'))
    print(date_format('12-10-2020'))
