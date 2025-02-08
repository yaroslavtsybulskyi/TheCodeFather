"""
Module for fetching JSON data from a web service.
"""

import requests


class WebService:
    """
    Class WebService which has method get_data that returns json response.
    """

    @staticmethod
    def get_data(url: str) -> dict:
        """
        Method which returns json
        :param url: url to get data from
        :return: data returned from url
        """
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
