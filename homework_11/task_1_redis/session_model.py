"""
Module: session_manager
-----------------------
This module provides a `SessionManager` class to handle user session management using Redis.
"""

import json
import time
import uuid
from datetime import datetime
from typing import Dict, Union

from redis import Redis, RedisError


class SessionManager:
    """
    Manages user sessions using Redis.
    This class allows creating, retrieving, updating, and deleting user sessions.
    Sessions are stored as JSON objects and automatically expire after a given TTL.
    """

    def __init__(self, redis_host="localhost", redis_port=6379, session_expiry=1800) -> None:
        """
        Initializes the SessionManager and connects to the Redis database.
        :param redis_host: Redis server hostname (default: "localhost").
        :param redis_port: Redis server port (default: 6379).
        :param session_expiry: Session expiration time in seconds (default: 1800s = 30 minutes).
        """
        self.redis = Redis(host=redis_host, port=redis_port, decode_responses=True)
        self.session_expiry = session_expiry

    def create_session(self, user_id: str) -> str:
        """
        Creates a new session using the given user id with a unique session token.
        :param user_id: The user's unique identifier.
        :return: Unique session token
        :raises TypeError: If user id is not a string.
        :raises RedisError: If case it is not possible to reach db.
        """
        if not isinstance(user_id, str):
            raise TypeError("User id must be a string.")

        session_token = str(uuid.uuid4())
        session_data = {
            "user_id": user_id,
            "session_token": session_token,
            "login_time": datetime.now().isoformat(),
            "last_activity": datetime.now().isoformat()
        }
        try:
            self.redis.setex(session_token, self.session_expiry, json.dumps(session_data))
            return session_token
        except RedisError as e:
            print(f"Error: {e}")
            return "Failed to create new session."

    def get_session(self, session_token: str) -> Union[Dict, None]:
        """
        Retrieves the session data for a given session token.
        :param session_token:  The session token to retrieve.
        :return: The session data as a dictionary if found, else None.
        :raises TypeError: If session_token is not a string.
        :raises RedisError: If case it is not possible to reach db.
        """
        if not isinstance(session_token, str):
            raise TypeError("Session token must be a string.")

        try:
            session_data = self.redis.get(session_token)
            return json.loads(session_data) if session_data else None
        except RedisError as e:
            print(f"Error: {e}")
            return None

    def update_session(self, session_token: str) -> str:
        """
        Updates the last activity timestamp of a session and refreshes its TTL.
        :param session_token: The session token to update.
        :return: Confirmation message indicating success or failure.
        :raises TypeError: If session_token is not a string.
        :raises RedisError: If case it is not possible to reach db.
        """
        if not isinstance(session_token, str):
            raise TypeError("Session token must be a string.")

        try:
            session_data = self.redis.get(session_token)

            if not session_data:
                return f"Session {session_token} was not found."

            session_data = json.loads(session_data)
            session_data["last_activity"] = datetime.now().isoformat()

            self.redis.setex(session_token, self.session_expiry, json.dumps(session_data))
            return f"Session {session_token} was successfully updated."
        except RedisError as e:
            print(f"Error: {e}")
            return "Failed to update last activity timestamp."

    def delete_session(self, session_token: str) -> str:
        """
        Deletes a session from Redis.
        :param session_token: The session token to delete.
        :return: Confirmation message indicating success or failure.
        :raises TypeError: If session_token is not a string.
        :raises RedisError: If case it is not possible to reach db.
        """
        if not isinstance(session_token, str):
            raise TypeError("Session token must be a string.")
        try:
            result = self.redis.delete(session_token)
            if not result:
                return f"Session {session_token} was not found."
            return f"Session {session_token} was successfully deleted."
        except RedisError as e:
            print(f"Error: {e}")
            return "Failed to delete session data."


if __name__ == "__main__":
    session_manager = SessionManager()
    session = session_manager.create_session("user1")
    print(session_manager.get_session(session))
    time.sleep(5)
    print(session_manager.update_session(session))
    print(session_manager.get_session(session))
    print(session_manager.delete_session(session))
    print(session_manager.get_session(session))
    print(session_manager.update_session(session))
    print(session_manager.delete_session(session))
