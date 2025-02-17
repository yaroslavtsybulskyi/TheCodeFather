"""
Model Operations Module
This module provides functions to work with actors and movies: add_movie, add_actors, get_actor_id
"""

from typing import List, Union

from homework_10.db import create_connection


def get_actor_id(name: str) -> Union[int, None]:
    """
    Retrieves the ID of an actor by their name.

    This function checks if the actor exists in the database and returns their ID.
    If the actor is not found, it returns `None`.

    :param name: The full name of the actor as a string.
    :raises TypeError: If the input `name` is not a string.
    :return: The unique ID of the actor if found, otherwise `None`.
    """
    if not isinstance(name, str):
        raise TypeError("Actor name must be a string")

    query = """SELECT id FROM actors WHERE name = ?"""
    with create_connection() as conn:
        cursor = conn.cursor()
        try:
            cursor.execute(query, (name,))
            result = cursor.fetchone()
            return result[0] if result else None
        finally:
            cursor.close()


def add_actor(name: str, birth_year: int = 1970) -> None:
    """
    This functions inserts a new actor into the database.
    :param name: name of the actor as a string.
    :param birth_year: birth year of the actor as an integer.

    :raises TypeError: If the input `name` is not a string.
    :raises TypeError: If the input `birth_year` is not an integer.
    """
    if not isinstance(name, str):
        raise TypeError("Actor name must be a string")
    if not isinstance(birth_year, int):
        raise TypeError("Birth year must be an integer")

    query = """INSERT INTO actors (name, birth_year) values (?, ?)"""
    with create_connection() as conn:
        cursor = conn.cursor()
        try:
            cursor.execute(query, (name, birth_year))
            conn.commit()
        finally:
            cursor.close()


def add_movie(title: str, release_year: int, genre: str, actors: List[str]) -> None:
    """
    Function to add a movie to the database.
    :param title: The title of the movie.
    :param release_year: release year of the movie.
    :param genre: genre of the movie.
    :param actors: List of actors.
    :raises TypeError: If the input `title` is not a string.
    :raises TypeError: If the input `release_year` is not an integer.
    :raises TypeError: If the input `genre` is not a string.
    :raises TypeError: If the input `actors` is not a list.
    """

    if not isinstance(title, str):
        raise TypeError("Movie title must be a string")
    if not isinstance(release_year, int):
        raise TypeError("Release year must be an integer")
    if not isinstance(genre, str):
        raise TypeError("Genre must be a string")
    if not isinstance(actors, list):
        raise TypeError("Actors must be a list")

    query_insert_movie = """INSERT INTO movies (title, release_year, genre) VALUES (?, ?, ?)"""
    query_insert_actor = """INSERT INTO movie_cast (movie_id, actor_id) VALUES (?, ?)"""
    query_insert_new_actor = """INSERT INTO actors (name, birth_year) VALUES (?, ?)"""

    with create_connection() as conn:
        cursor = conn.cursor()
        try:
            cursor.execute(query_insert_movie, (title, release_year, genre))
            movie_id = cursor.lastrowid

            for actor in actors:
                actor_id = get_actor_id(actor)
                if actor_id is None:
                    cursor.execute(query_insert_new_actor, (actor, 1970))
                    actor_id = cursor.lastrowid
                cursor.execute(query_insert_actor, (movie_id, actor_id))

            conn.commit()
        finally:
            cursor.close()
