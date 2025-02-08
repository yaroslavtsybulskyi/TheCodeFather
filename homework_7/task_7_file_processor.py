"""
File Processing Utility

This module provides a `FileProcessor` class for reading from and writing to files.
"""

import os


class FileProcessor:
    """
    A utility class for handling file reading and writing.
    """

    @staticmethod
    def write_to_file(filepath: str, data: str) -> None:
        """
        Writes the provided data to a file.

        :param filepath: The path of the file to write to.
        :param data: The content to write to the file.
        :raises TypeError: If `data` is not a string.
        :raises OSError: If an error occurs while writing the file.
        """
        if not isinstance(data, str):
            raise TypeError('data must be a string')
        try:
            with open(filepath, "w", encoding='utf-8') as file:
                file.write(data)
        except IOError as e:
            raise IOError(f"Failed to write to {filepath}: {e}")

    @staticmethod
    def read_from_file(filepath: str) -> str:
        """
        Reads the contents of a file and returns it as a string.
        :param filepath: The path of the file to read from.
        :return: The content of the file as a string.
        :raises FileNotFoundError: If the file does not exist.
        :raises OSError: If an error occurs while reading the file.
        """
        if not os.path.isfile(filepath):
            raise FileNotFoundError('File not found')
        try:
            with open(filepath, "r", encoding='utf-8') as file:
                return file.read()
        except IOError as e:
            raise IOError(f"Failed to read from {filepath}: {e}")
