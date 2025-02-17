"""
Utils Module
This module includes function `movie_age` which returns the age of the movie
"""

from datetime import datetime


def movie_age(release_year: int) -> int:
    """
    Returns the age of the movie
    :param release_year: The release year of the movie
    :return: the age of the movie
    :raise TypeError: If `release_year` is not an integer
    :raise ValueError: If `release_year` is less than 1910
    """

    if not isinstance(release_year, int):
        raise TypeError("Release year must be an integer")
    if release_year < 1910:
        raise ValueError("Release year must be greater than 1910")

    current_year = datetime.now().year
    return current_year - release_year
