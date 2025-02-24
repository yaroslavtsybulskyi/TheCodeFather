"""
Module: base_repository
-----------------------
This module defines the BaseRepository class, which provides a generic
interface for interacting with MongoDB collections.
"""

from typing import Dict, Any, List, Optional

import pymongo

from pymongo.errors import PyMongoError


class BaseRepository:
    """
    A generic repository class for performing common database operations in MongoDB.
    This class provides methods to insert, retrieve, update, and delete
    documents from a specified collection.
    Attributes:
        client (MongoClient): The MongoDB client instance.
        db (Database): The database instance.
        collection (Collection): The collection instance within the database.
    """

    def __init__(self, db_name: str, collection_name: str) -> None:
        """
         Initializes the repository by connecting to MongoDB.
        :param db_name: The name of the MongoDB database.
        :param collection_name: The name of the collection to interact with.
        :raises TypeError: If `db_name` is not a string.
        :raises TypeError: If `collection_name` is not a string.
        """
        if not isinstance(db_name, str):
            raise TypeError("Database name must be a string")
        if not isinstance(collection_name, str):
            raise TypeError("Collection name must be a string")

        self.client = pymongo.MongoClient("mongodb://localhost:27017/")
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]

    def insert_one(self, data: Dict[str, Any]) -> Optional[pymongo.results.InsertOneResult]:
        """
        Inserts a single document into the collection.
        :param data: The document to insert.
        :return: The result of the insertion.
        :raises pymongo.errors.PyMongoError: If there is an error in inserting data.
        :raises TypeError: If `data` is not a dictionary.
        """
        if not isinstance(data, dict):
            raise TypeError("Data must be a dictionary")

        try:
            return self.collection.insert_one(data)
        except PyMongoError as e:
            print(f"Error: {e}")
            return None

    def insert_many(self, data: List[Dict[str, Any]]) -> Optional[pymongo.results.InsertManyResult]:
        """
        Inserts a list of documents into the collection.
        :param data: list of documents to insert.
        :return:  result of the insertion.
        :raises pymongo.errors.PyMongoError: If there is an error in inserting data.
        :raises TypeError: If `data` is not a list.
        """
        if not isinstance(data, list):
            raise TypeError("Data must be a list")
        try:
            return self.collection.insert_many(data)
        except PyMongoError as e:
            print(f"Error: {e}")
            return None

    def find_one(self, query: Optional[Dict[str, Any]] = None) -> Optional[Dict[str, Any]]:
        """
        Retrieves a single document from the collection.
        :param query: The filter criteria for the search. Defaults to None.
        :return: The first matching document, or None if no match is found.
        :raises pymongo.errors.PyMongoError: If there is an error in retrieving data.
        :raises TypeError: If `query` is not a dictionary.
        """
        if query is not None and not isinstance(query, dict):
            raise TypeError("Query must be a dictionary or None")

        try:
            return self.collection.find_one(query)
        except PyMongoError as e:
            print(f"Error: {e}")
            return None

    def find_all(self, query: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        """
        Retrieves all documents from the collection.
        :param query: The filter criteria for the search. Defaults to None.
        :return: All documents from the collection matching criteria.
        :raises pymongo.errors.PyMongoError: If there is an error in retrieving data.
        :raises TypeError: If `query` is not a dictionary.
        """
        if query is not None and not isinstance(query, dict):
            raise TypeError("Query must be a dictionary or None")

        try:
            return list(self.collection.find(query))
        except PyMongoError as e:
            print(f"Error: {e}")
            return []

    def update_one(self, query: Dict[str, Any], new_data: Dict[str, Any]) \
            -> Optional[pymongo.results.UpdateResult]:
        """
        Updates a single document that matches the query.
        :param query: The filter criteria for the search.
        :param new_data: The data to insert.
        :return: The result of the update operation.
        :raises pymongo.errors.PyMongoError: If there is an error in updating data.
        :raises TypeError: If `query` is not a dictionary.
        :raises TypeError: If `new_data` is not a dictionary.
        """
        if not isinstance(query, dict):
            raise TypeError("Query must be a dictionary")
        if not isinstance(new_data, dict):
            raise TypeError("New data must be a dictionary")

        try:
            return self.collection.update_one(query, {"$set": new_data})
        except PyMongoError as e:
            print(f"Error: {e}")
            return None

    def delete_one(self, query: Dict[str, Any]) -> Optional[pymongo.results.DeleteResult]:
        """
        Deletes a single document from the collection that matches the query.
        :param query: The filter criteria for the deletion.
        :return: The filter criteria for the deletion.
        :raises pymongo.errors.PyMongoError: If there is an error in deleting data.
        :raises TypeError: If `query` is not a dictionary.
        """
        if not isinstance(query, dict):
            raise TypeError("Query must be a dictionary")
        try:
            return self.collection.delete_one(query)
        except PyMongoError as e:
            print(f"Error: {e}")
            return None
