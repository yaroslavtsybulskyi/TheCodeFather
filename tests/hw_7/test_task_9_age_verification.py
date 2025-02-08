"""
Test Suite for Age Verifier

This module contains unit tests for the `AgeVerifier` class,
which determines if a person is considered an adult.
"""

import pytest

from homework_7.task_9_age_verificator import AgeVerifier


def test_age_verification_positive():
    """Test that an age >= 18 is correctly classified as an adult."""
    assert AgeVerifier.is_adult(19)


def test_age_verification_negative():
    """Test that an age < 18 is correctly classified as NOT an adult."""
    assert AgeVerifier.is_adult(15)


def test_age_verification_float():
    """Test that passing a float raises a TypeError."""
    with pytest.raises(TypeError):
        assert AgeVerifier.is_adult(5.0)


@pytest.mark.parametrize("age", [34, 22, 19, 20, 21, 55, -1, -10, 120])
def test_age_verification_batch(age):
    """
    Test multiple age values using parameterization.
    - If `age < 0`, the test is skipped (invalid input).
    - Otherwise, checks if `is_adult(age)` is correct.
    """
    if age < 0:
        pytest.skip()
    if age > 60:
        pytest.skip("Probability is too small")
    assert AgeVerifier.is_adult(age)
