"""
Repository Pattern Module

This module demonstrates:
    - `FinalClass` metaclass to prevent inheritance.
    - `Config` class using `FinalClass` to be non-inheritable.
    - `BaseRepository` as an Abstract Base Class (ABC) enforcing `save(data: Dict[str, Any])`.
    - `SQLRepository` implementing `BaseRepository`.
"""

from abc import ABC, abstractmethod
from typing import Dict, Any


class FinalClass(type):
    """
    Metaclass that prevents inheritance.
    """

    def __init__(cls, name, bases, attrs):
        """
        Constructor.
        """
        super().__init__(name, bases, attrs)
        for base in bases:
            if isinstance(base, FinalClass):
                raise TypeError("Inheritance is prohibited from final class")


class Config(metaclass=FinalClass):
    """
    Configuration class with FinalClass metaclass.
    """
    pass


class BaseRepository(ABC):
    """
    Abstract Base Class for repositories.
    This class enforces a `save()` method that must be implemented in child classes.
    """

    @abstractmethod
    def save(self, data: Dict[str, Any]) -> None:
        """
        Abstract method that must be implemented by subclasses.
        :param data: data to be saved.
        """
        pass


class SQLRepository(BaseRepository):
    """
    Implementation of SQLRepository class.
    """

    def __init__(self) -> None:
        """Constructor"""
        self.data = {}

    def save(self, data: Dict[str, Any]) -> None:
        """
        Method that saves data
        :param data: data to be saved.
        """
        self.data = data


if __name__ == "__main__":
    repo = SQLRepository()
    repo.save({"name": "Product1", "price": 10.5})

    try:
        class MyConfig(Config):
            pass
    except TypeError as e:
        print(e)
