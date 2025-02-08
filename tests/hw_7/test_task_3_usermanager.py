"""
Test suite for the UserManager class using pytest.

This module contains unit tests for the `UserManager` class, verifying the
correct functionality of adding, removing, and retrieving users.
"""

import pytest

from homework_7.task_3_users import UserManager


@pytest.fixture
def user_manager():
    """
    Pytest fixture that initializes a UserManager instance with predefined users.

    This fixture creates an instance of `UserManager` and adds:
    - Alice (30 years old)
    - Bob (25 years old)
    :return: instance of `UserManager` with predefined users
    """
    um = UserManager()
    um.add_user("Alice", 30)
    um.add_user("Bob", 25)
    return um


def test_add_user(user_manager):
    """Test adding a new user to the UserManager."""
    user_manager.add_user("Derek", 22)
    assert ("Derek", 22) in user_manager.get_users()


def test_remove_user(user_manager):
    """ Test removing an existing user from the UserManager."""
    user_manager.remove_user("Alice")
    assert ("Alice", 30) not in user_manager.get_users()


@pytest.mark.skipif(lambda: len(user_manager().get_users()) < 3, reason="not enough users")
def test_user_exists(user_manager):
    """
    Test to check if "Alice" exists in the user list.
    This test is skipped if there are fewer than 3 users.
    """
    assert ("Alice", 30) in user_manager.get_users()


@pytest.mark.skipif(lambda: ("Derek", 22) in user_manager().get_users(), reason="Derek in the list")
def test_users(user_manager):
    """
    Test that "Bob" exists in the user list.
    This test is skipped if "Derek" (22) is already in the user list.
    """
    assert ("Bob", 25) in user_manager.get_users()


def test_get_all_users(user_manager):
    """
    Test retrieving all users.
    """
    assert [('Alice', 30), ('Bob', 25)] == user_manager.get_users()


def test_get_users_user_not_added(user_manager):
    """
    Test adding and removing a user to check if they are no longer in the list.
    """
    user_manager.add_user("Derek", 22)
    user_manager.remove_user("Derek")
    assert ("Derek", 22) not in user_manager.get_users()
