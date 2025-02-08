"""
Test Suite for FileProcessor

This module contains unit tests for the `FileProcessor` class,
focusing on file writing, reading, handling large data, and exception handling.
"""

import pytest

from homework_7.task_7_file_processor import FileProcessor


def test_write_to_and_read_file(tmpdir):
    """Test writing to and reading from a file."""
    file = tmpdir.join('test.txt')

    FileProcessor.write_to_file(str(file), "Test")
    assert file.read() == "Test"


def test_read_from_not_existing_file(tmpdir):
    """Test reading a non-existing file should raise FileNotFoundError."""
    file = tmpdir.join('test.txt')
    with pytest.raises(FileNotFoundError):
        FileProcessor.read_from_file(str(file))


def test_read_empty_file(tmpdir):
    """Test reading from an empty file."""
    file = tmpdir.join('empty.txt')
    FileProcessor.write_to_file(str(file), "")
    assert file.read() == ""


def test_read_big_file(tmpdir):
    """Test handling of large file reading (1MB)."""
    file = tmpdir.join('big_file.txt')
    large_data = 'A' * (1024 * 10)
    FileProcessor.write_to_file(str(file), large_data)
    assert file.read() == large_data


def test_write_not_string_data(tmpdir):
    """Test that writing non-string data raises TypeError."""
    file = tmpdir.join('test.txt')
    with pytest.raises(TypeError):
        FileProcessor.write_to_file(str(file), 5)
