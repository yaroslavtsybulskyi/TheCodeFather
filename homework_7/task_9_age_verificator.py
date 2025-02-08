"""
Age Verification Module

This module provides class AgeVerifier for checking age (if adult)

"""


class AgeVerifier:
    """
    Class AgeVerifier for age verification.
    """

    @staticmethod
    def is_adult(age: int) -> bool:
        """
        Checks if age is adult
        :param age: age to check
        :return: returns boolean value if age is greater/equal than 18
        :raises: ValueError if age is not an integer number
        :raises: TypeError if age is less than 0
        """
        if not isinstance(age, int):
            raise TypeError('Age must be an integer')
        if age < 0:
            raise ValueError('Age cannot be negative')

        return age >= 18
