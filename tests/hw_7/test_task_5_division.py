"""
Test Suite for the divide function.

This module contains unit tests for the `divide` function from `homework_7.task_5_division`.
The tests cover:
    - Division by zero (`ZeroDivisionError`).
    - Handling of incorrect types (`TypeError`).
    - Correct division results using parameterized tests.
"""

import pytest

from homework_7.task_5_division import divide


def test_divide_zero():
    """Test that dividing by zero raises a ZeroDivisionError."""
    with pytest.raises(ZeroDivisionError):
        divide(5, 0)


def test_divide_number_to_float():
    """Test that passing a string as a numerator raises a TypeError."""
    with pytest.raises(TypeError):
        divide("7", 5)


def test_divide_number_to_string():
    """Test that passing a string as a denominator raises a TypeError."""
    with pytest.raises(TypeError):
        divide(5, "5.4")


@pytest.mark.parametrize("a, b, expected",
                         [(5, 1, 5),
                          (-2, 1, -2),
                          (3, 2, 1.5),
                          (100, 10, 10),
                          (14, 7, 2)])
def test_division_positive(a, b, expected):
    """Test division with valid integer inputs using parameterized tests."""
    assert divide(a, b) == expected
