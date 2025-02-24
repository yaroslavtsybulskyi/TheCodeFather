"""
Module: product_repository
--------------------------
This module defines the ProductRepository class, responsible for managing
product-related operations in the MongoDB 'products' collection.
"""

from typing import Optional

import pymongo
from pymongo.errors import PyMongoError

from base_repo import BaseRepository


class ProductRepository(BaseRepository):
    """
    Repository class for handling product-related database operations in the 'products' collection.
    """

    def __init__(self) -> None:
        """
        Initializes the ProductRepository, setting up the connection to the 'products' collection.
        """
        super().__init__("my_shop", "products")

    def update_stock(self, product_name: str, quantity: int) -> Optional[pymongo.results.UpdateResult]:
        """
        Updates the stock quantity for a given product.
        :param product_name: The name of the product
        :param quantity: The new stock quantity (must be >= 0).
        :return: The result of the update operation.
        :raises ValueError: If `quantity` is less than 0.
        """
        if quantity < 0:
            raise ValueError("Quantity must be greater than  or equal to 0")

        return self.update_one({"name": product_name}, {"stock": quantity})

    def delete_out_of_stock(self) -> Optional[pymongo.results.DeleteResult]:
        """
        Deletes all products that have a stock quantity of zero.
        :return: The result of the delete operation.
        """
        return self.delete_many({"stock": 0})

    def create_index(self) -> None:
        """
        Creates an index on the 'category' field for better query performance.
        :raises pymongo.errors.PyMongoError: Error in connecting to MongoDB or processing data.
        """
        try:
            self.collection.create_index([("category", 1)])
        except PyMongoError as e:
            print(f"Error: {e}")
