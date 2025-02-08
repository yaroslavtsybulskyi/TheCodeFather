"""
Tests for Homework 7 Task 1
"""

import unittest
from homework_7.task_1_string_processor import StringProcessor


class TestHomeworkTaskSeven(unittest.TestCase):
    """
    Tests Class for running tests
    """

    def setUp(self):
        """Initialize a new StringProcessor instance for each test."""
        self.string_processor = StringProcessor()

    @unittest.skip("Known issue, will be resolved later")
    def test_reverse_string_empty_string(self):
        """Skipping test due to a known issue."""
        self.assertEqual(self.string_processor.reverse_string(""), "")

    def test_reverse_string_positive_case(self):
        """Test reversing a regular string."""
        self.assertEqual(self.string_processor.reverse_string("James"), "semaJ")

    def test_reverse_string_negative_case(self):
        """Test that the reversed result is not incorrect."""
        self.assertNotEqual(self.string_processor.reverse_string("Jameson"), "n0semaJ")

    def test_reverse_string_difference_register(self):
        """Test reversing a string with mixed case letters and spaces."""
        self.assertEqual(self.string_processor.reverse_string("UnItTeSt iS 1"), '1 Si tSeTtInU')

    def test_reverse_string_integer_number(self):
        """Test that passing an integer raises a TypeError."""
        with self.assertRaises(TypeError):
            self.string_processor.reverse_string(1)

    def test_capitalize_string_positive_case(self):
        """Test capitalizing a normal sentence."""
        self.assertEqual(self.string_processor.capitalize_string("who is this?"), "Who is this?")

    def test_capitalize_string_with_leading_space(self):
        """Test capitalizing a string that starts with a space (should remain unchanged)."""
        self.assertEqual(self.string_processor.capitalize_string(" space first"), " space first")

    def test_capitalize_string_number(self):
        """Test capitalizing a string that starts with a non-alphabetic character."""
        self.assertEqual(self.string_processor.capitalize_string("1"), '1')

    def test_capitalize_string_integer(self):
        """Test that passing an integer raises a TypeError."""
        with self.assertRaises(TypeError):
            self.string_processor.capitalize_string(1)

    def test_count_vowels_positive_case(self):
        """Test counting vowels in a regular word."""
        self.assertEqual(self.string_processor.count_vowels("Hello"), 2)

    def test_count_vowels_string_integer(self):
        """Test counting vowels in a string that contains only numbers."""
        self.assertEqual(self.string_processor.count_vowels("123345323"), 0)

    def test_count_vowels_integer(self):
        """Test that passing an integer raises a TypeError."""
        with self.assertRaises(TypeError):
            self.string_processor.count_vowels(1)


if __name__ == '__main__':
    unittest.main()
