"""
Module: event_logger
---------------------
This module provides an `EventLogger` class for managing event logs using Apache Cassandra.
"""

import uuid
from datetime import datetime, timedelta

from cassandra import DriverException
from cassandra.cluster import Cluster


class EventLogger:
    """
    Manages event logs using Cassandra.
    """

    def __init__(self, host="127.0.0.1", keyspace="event_logs") -> None:
        """
        Initializes the Cassandra connection and creates a keyspace and table if they don't exist.
        :param host: The Cassandra host (default: "127.0.0.1").
        :param keyspace: The Cassandra keyspace to use (default: "event_logs").
        :raises DriverException: If the connection cannot be established.
        """
        try:
            self.cluster = Cluster([host])
            self.session = self.cluster.connect()

            self.session.execute(f"""
                CREATE KEYSPACE IF NOT EXISTS {keyspace}
                WITH replication = {{'class': 'SimpleStrategy', 'replication_factor': 1}};
            """)

            self.session.set_keyspace(keyspace)

            self.session.execute("""
                CREATE TABLE IF NOT EXISTS event_logs (
                    event_id UUID PRIMARY KEY,
                    user_id TEXT,
                    event_type TEXT,
                    timestamp TIMESTAMP,
                    metadata TEXT
                );
            """)
        except DriverException as e:
            print(f"Error: {e}")

    def create_event(self, user_id: str, event_type: str, metadata: str) -> str:
        """
        Inserts a new event log.
        :param user_id: The ID of the user.
        :param event_type: The type of event.
        :param metadata: metadata of the event.
        :return: The generated event_id, or an error message if insertion fails
        """
        if not all(isinstance(arg, str) for arg in [user_id, event_type, metadata]):
            raise TypeError("All arguments must be strings.")

        event_id = uuid.uuid4()
        timestamp = datetime.now()

        query = """
            INSERT INTO event_logs (event_id, user_id, event_type, timestamp, metadata)
            VALUES (%s, %s, %s, %s, %s);
        """
        try:
            self.session.execute(query, (event_id, user_id, event_type, timestamp, metadata))
            return str(event_id)
        except DriverException as e:
            print(f"Error: {e}")
            return "Failed to insert new event log."

    def get_events_for_last_24_hours(self, event_type: str) -> list:
        """
        Retrieves events of a given type from the last 24 hours.
        :param event_type: type of the event to be retrieved.
        :return: List of event records, or an empty list if an error occurs.
        :raises DriverException: If the connection cannot be established.
        :raises TypeError: If the type of the event is not a string.
        """
        if not isinstance(event_type, str):
            raise TypeError("Event type must be a string.")

        query = """SELECT * FROM event_logs WHERE event_type  = %s AND timestamp >= %s"""

        since_time = datetime.now() - timedelta(days=1)
        params = (event_type, since_time)
        try:
            result = self.session.execute(query, params)
            return [row.as_dict() for row in result]
        except DriverException as e:
            print(f"Error: {e}")
            return []

    def update_event_metadata(self, event_id: str, metadata: str) -> str:
        """
        Updates the metadata of a given event.
        :param event_id: Event ID to update metadata for.
        :param metadata: new metadata to update.
        :return: Confirmation message, or an error message if update fails.
        :raises DriverException: If the connection cannot be established.
        :raises TypeError: If the arguments are not strings.
        """
        if not all(isinstance(args, str) for args in [event_id, metadata]):
            raise TypeError("All arguments must be strings.")

        query = "UPDATE event_logs SET metadata = %s WHERE event_id = %s"
        try:
            self.session.execute(query, (metadata, uuid.UUID(event_id)))
            return f"{event_id} metadata was successfully updated"
        except DriverException as e:
            print(f"Error: {e}")
            return "Failed to update event metadata."

    def delete_old_events(self) -> str:
        """
        Deletes all events older than 7 days.
        :return: Confirmation message, or an error message if deletion fails.
        """
        delete_time = datetime.now() - timedelta(days=7)
        query = "DELETE FROM event_logs WHERE timestamp < %s"
        try:
            self.session.execute(query, (delete_time,))
            return "Events older than 7 days deleted."
        except DriverException as e:
            print(f"Error: {e}")
            return "Failed to delete old events."


if __name__ == "__main__":
    data = EventLogger()
    log_1 = data.create_event('user_001', 'LOGIN', 'Success')
    log_2 = data.create_event('user_001', 'OPEN_PAGE', 'Success')
    log_3 = data.create_event('user_002', 'LOGIN', 'Success')

    print(data.get_events_for_last_24_hours('LOGIN'))

    data.update_event_metadata(log_1, 'Invalid Password')
    data.delete_old_events()
