"""
User Management Module

This module provides a `UserManager` class for managing users by adding,
removing, and retrieving user data. The users are stored in a dictionary
where each key is a user's name, and the value is their age.

Classes:
    - UserManager: Handles adding, removing, and retrieving users.
"""


class UserManager:
    """
    A class to manage users by adding, removing, and retrieving user data.

    This class maintains a dictionary of users where:
    - The key is the user's name (string).
    - The value is the user's age (integer).

    Methods:
    - add_user(name, age): Adds a user to the system.
    - remove_user(name): Removes a user from the system.
    - get_users(): Returns a list of all users.
    """

    def __init__(self):
        """Initializes an empty dictionary to store users."""
        self.users = {}

    def add_user(self, name: str, age: int) -> None:
        """
        Adds a new user to the system.
        :param name: The name of the user.
        :param age: The age of the user.
        :raises ValueError: If the user already exists.
        """
        if name in self.users:
            raise ValueError(f'User {name} already exists')
        self.users[name] = age

    def remove_user(self, name: str) -> None:
        """
        Removes a user from the system.
        :param name: the name of the user.
        :raises ValueError: If the user does not exist.
        """
        if name not in self.users:
            raise ValueError(f'User {name} does not exist')
        del self.users[name]

    def get_users(self) -> list:
        """
        Returns a list of all users.
        :return: list of all users.
        """
        return list(self.users.items())
