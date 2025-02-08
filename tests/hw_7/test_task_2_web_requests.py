"""
Unit tests for WebService class.

This module tests the WebService.get_data() method using unittest and unittest.mock
to simulate HTTP requests with various response statuses (200, 404, 500).
"""
import unittest

from unittest.mock import patch

import requests

from homework_7.task_2_web_requests import WebService


class TestWebService(unittest.TestCase):
    """
    Test suite for the WebService class.
    """

    def setUp(self):
        """Initializes an instance of WebService before each test."""
        self.web_service = WebService()

    @patch('requests.get')
    def test_request_200(self, mock_get):
        """
        Tests if get_data() correctly handles a successful HTTP 200 response.

        - Mocks `requests.get()` to return status_code 200.
        - Mocks `response.json()` to return {"data": "test"}.
        - Asserts that the correct data is returned.
        - Ensures `requests.get()` is called once with the correct URL.
        """
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {"data": "test"}
        result = self.web_service.get_data('https://example.com')
        self.assertEqual(result, {"data": "test"})
        mock_get.assert_called_once_with('https://example.com')

    @patch('requests.get')
    def test_request_404(self, mock_get):
        """
        Tests if get_data() correctly handles an HTTP 404 Not Found error.

        - Mocks `requests.get()` to return status_code 404.
        - Mocks `raise_for_status()` to raise an HTTPError.
        - Ensures that `get_data()` raises requests.exceptions.HTTPError.
        - Verifies that the exception message contains "404 Not Found".
        - Ensures `requests.get()` is called once with the correct URL.
        """
        mock_get.return_value.status_code = 404
        mock_get.return_value.raise_for_status.side_effect = (
            requests.exceptions.HTTPError("404 Not Found"))

        with self.assertRaises(requests.exceptions.HTTPError) as context:
            self.web_service.get_data('https://example.com')

        self.assertEqual(str(context.exception), "404 Not Found")

        mock_get.assert_called_once_with('https://example.com')

    @patch('requests.get')
    def test_request_500(self, mock_get):
        """
        Tests if get_data() correctly handles an HTTP 500 Internal Server Error.

        - Mocks `requests.get()` to return status_code 500.
        - Mocks `raise_for_status()` to raise an HTTPError.
        - Ensures that `get_data()` raises requests.exceptions.HTTPError.
        - Verifies that the exception message contains "500 Server Error".
        - Ensures `requests.get()` is called once with the correct URL.
        """
        mock_get.return_value.status_code = 500
        mock_get.return_value.raise_for_status.side_effect = (
            requests.exceptions.HTTPError("500 Server Error"))

        with self.assertRaises(requests.exceptions.HTTPError) as context:
            self.web_service.get_data('https://example.com')

        self.assertEqual(str(context.exception), "500 Server Error")

        mock_get.assert_called_once_with('https://example.com')


if __name__ == '__main__':
    unittest.main()
