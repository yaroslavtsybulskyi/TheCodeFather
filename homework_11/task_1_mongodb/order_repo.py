"""
Module: order_repository
------------------------
This module contains the OrderRepository class, which interacts with the MongoDB
'orders' collection.
"""

from datetime import datetime, timedelta
from typing import List, Dict, Any

from pymongo.errors import PyMongoError
from base_repo import BaseRepository


class OrderRepository(BaseRepository):
    """
    Repository class for handling orders in the 'orders' collection.

    Provides methods for retrieving recent orders, fetching sales information,
    and calculating total order amounts for clients.
    """

    def __init__(self) -> None:
        """
        Initializes the OrderRepository with the 'orders' collection.
        """
        super().__init__("my_shop", "orders")

    def get_recent_orders(self, days: int = 30) -> List[Dict[str, Any]]:
        """
        Retrieves recent orders within the past `days`.
        :param days: number of days to get recent orders for.
        :return: A list of recent orders within the given timeframe. Default is 30 days.
        :raises TypeError: If `days` is not an integer.
        """
        if not isinstance(days, int):
            raise TypeError("Days must be an integer")
        return self.find_all({"date": {"$gt": datetime.today() - timedelta(days=days)}})

    def get_sales_info(self, start_date: datetime.date = datetime.today() - timedelta(days=10),
                       end_date: datetime.date = datetime.today()) -> List[Dict[str, Any]]:
        """
        Retrieves total sales per product within a specified date range.
        :param start_date: The start of the date range. Defaults to 10 days ago.
        :param end_date: The end of the date range. Defaults to today.
        :return: A list containing sales information for each product.
        :raises TypeError: If `start_date` or `end_date` is not a datetime.
        :raises pymongo.errors.PyMongoError: Error in connecting to MongoDB or processing data.
        """
        if not isinstance(start_date, datetime) or not isinstance(end_date, datetime):
            raise TypeError("Start date and end date must be of type datetime.date")

        try:
            return list(self.collection.aggregate([
                {"$match": {"date": {"$gte": start_date, "$lte": end_date}}},
                {"$unwind": "$products"},
                {"$group": {"_id": "$products.name", "total_sold": {"$sum": "$products.quantity"}}}
            ]))
        except PyMongoError as e:
            print(f"Error: {e}")
            return []

    def get_total_order_amount_by_client(self, client_name: str) -> float:
        """
        Calculates the total amount spent by a given client.
        :param client_name: The name of the client.
        :return: The total amount spent by the client.
        :raises TypeError: If `client_name` is not a string.
        :raises pymongo.errors.PyMongoError: Error in connecting to MongoDB or processing data.
        """
        if not isinstance(client_name, str):
            raise TypeError("Client name must be a string")

        try:
            result = list(self.collection.aggregate([
                {"$match": {"client": client_name}},
                {
                    "$group": {
                        "_id": None,
                        "total_amount": {"$sum": "$total"}
                    }
                }
            ]))
            return result[0]["total_amount"] if result else 0.0
        except PyMongoError as e:
            print(f"Error: {e}")
            return 0.0
