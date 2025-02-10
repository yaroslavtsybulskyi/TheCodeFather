"""
User Management Module

This module defines:
    - A `TypedDict` named `User` to represent user data.
    - A `Protocol` named `UserDatabase` to define required database methods.
    - An `InMemoryUserDB` class that implements `UserDatabase` as an in-memory user store.
"""

from typing import TypedDict, Protocol, Optional, Dict


class User(TypedDict):
    """
    Represents a user with an ID, name, and admin status.

    Fields:
    - id (int): Unique user ID.
    - name (str): User's name.
    - is_admin (bool): Whether the user has admin privileges.
    """
    id: int
    name: str
    is_admin: bool


class UserDatabase(Protocol):
    """
    Defines the structure for a user database.

    Methods:
    - get_user(user_id: int) -> Optional[User]: Retrieves a user by ID.
    - save_user(user: User) -> None: Saves a user.
    """

    def get_user(self, user_id: int) -> Optional[User]:
        """
        Get user by id.
        :param user_id: User ID.
        """
        pass

    def save_user(self, user: User) -> None:
        """
        Save user to db
        :param user: User to save.
        """
        pass


class InMemoryUserDB:
    """
    An in-memory user database implementing the UserDatabase protocol.

    Methods:
    - get_user(user_id: int) -> Optional[User]: Returns a user or None if not found.
    - save_user(user: User) -> None: Stores a user in the database.
    """

    def __init__(self) -> None:
        """
        Initialize an in-memory user database.
        """
        self.users: Dict[int, User] = {}

    def get_user(self, user_id: int) -> Optional[User]:
        """
        Get user by id.
        :param user_id: User ID.
        """
        return self.users.get(user_id)

    def save_user(self, user: User) -> None:
        """
        Save user to db
        :param user: User to save.
        """
        self.users[user['id']] = user


if __name__ == "__main__":
    db = InMemoryUserDB()
    db.save_user({"id": 1, "name": "Alice", "is_admin": False})
    print(db.get_user(1))
    print(db.get_user(2))
