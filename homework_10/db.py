"""
Database Operations
Module is responsible for handling database operations.
"""

import sqlite3

from sqlite3 import Connection
from homework_10.utils import movie_age


def create_connection() -> Connection | None:
    """
    Creates a database connection and registers SQLite functions.
    :return: sqlite3.Connection
    :raises: sqlite3.OperationalError in case of database operation error.
    """
    try:
        conn = sqlite3.connect("moviebase.db", check_same_thread=False, timeout=10)
        conn.execute("PRAGMA journal_mode=WAL;")
        conn.create_function("movie_age", 1, movie_age)
        return conn
    except sqlite3.OperationalError:
        print("Database connection failed.")


def create_tables() -> None:
    """
    Creates tables movies, actors, and movie_cast in db in case they were not created yet.
    :raises: sqlite3.OperationalError in case of database operation error.
    :raises: sqlite3.IntegrityError in case of foreign key error.
    """
    sql_script = """
                CREATE TABLE IF NOT EXISTS movies (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                release_year INTEGER NOT NULL,
                genre TEXT NOT NULL);

                CREATE TABLE IF NOT EXISTS actors (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                birth_year INTEGER);

                CREATE TABLE IF NOT EXISTS movie_cast (
                movie_id INTEGER,
                actor_id INTEGER,
                PRIMARY KEY (movie_id, actor_id),
                FOREIGN KEY (movie_id) REFERENCES movies (id) ON DELETE CASCADE,
                FOREIGN KEY (actor_id) REFERENCES actors (id) ON DELETE CASCADE
                );
                """
    try:
        with create_connection() as conn:
            cursor = conn.cursor()
            cursor.executescript(sql_script)
            conn.commit()
    except sqlite3.IntegrityError:
        print("Foreign Key constraint failed.")
