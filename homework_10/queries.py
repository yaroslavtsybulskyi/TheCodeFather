"""
Queries Module
This module provides the list of queries to access the data
"""

from homework_10.db import create_connection


def get_movies_with_actors() -> None:
    """
    Gets all movies with actors.
    """
    query = """
         SELECT movies.title, GROUP_CONCAT(actors.name, ', ') AS actors
         FROM movies
         INNER JOIN movie_cast ON movies.id = movie_cast.movie_id
         INNER JOIN actors ON actors.id = movie_cast.actor_id
         GROUP BY movies.id
         """

    with create_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(query)
        result = cursor.fetchall()

        if result:
            for row in result:
                print(f"Movie: {row[0]}| Actors: {row[1]}")
        else:
            print("No movies found.")


def get_unique_genres() -> None:
    """
    Gets all unique genres.
    """
    query = """SELECT DISTINCT genre FROM movies"""

    with create_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(query)
        movies = cursor.fetchall()
        result = [movie[0] for movie in movies]
        if result:
            for genre in result:
                print(f"{genre}")
        else:
            print("No genres found.")


def get_movie_count_by_genre() -> None:
    """
    Gets movie count by genre.
    """
    query = """
    SELECT genre, COUNT(*) AS movies_count
    FROM movies
    GROUP BY genre
    """

    with create_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(query)
        genre_count = cursor.fetchall()
        if genre_count:
            for genre, count in genre_count:
                print(f"{genre}: {count}")
        else:
            print("No genres found.")


def get_average_age_by_genre(genre: str) -> None:
    """
    Gets average age of actors in movies by genre.
    :param genre: genre to check
    :raises TypeError: if genre is not a string.
    """
    if not isinstance(genre, str):
        raise TypeError("Genre must be a string.")

    query = """
    SELECT AVG(strftime('%Y', 'now') - actors.birth_year) AS avg_age
    FROM ACTORS
    JOIN movie_cast ON movie_cast.actor_id = actors.id
    JOIN movies ON movies.id = movie_cast.movie_id
    WHERE movies.genre = ?
    """

    with create_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(query, (genre,))
        result = cursor.fetchone()
        if result:
            print(f"{genre}: {result[0]}")
        else:
            print("No genres found.")


def search_movies_with_like(title: str) -> None:
    """
    Searches for movies with a certain title or partially
    :param title: title to search for
    :raises TypeError: if title is not a string.
    """
    if not isinstance(title, str):
        raise TypeError("Title must be a string.")

    query = """
    SELECT title from movies
    WHERE LOWER(title) LIKE LOWER (?)
    """

    with create_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(query, (f'%{title}%',))
        movies = cursor.fetchall()
        if movies:
            for movie in movies:
                print(f"{movie[0]}")
        else:
            print("No movies found.")


def get_movies_with_limit(limit: int, offset: int) -> None:
    """
    Gets list of movies with a certain pagination
    :param limit: limit of records to show
    :param offset: number of the page to show
    :raises TypeError: if limit is not an integer.
    :raises TypeError: if offset is not an integer.
    :raises ValueError: if offset is less than 1.
    :raises ValueError: if limit is less than 1.
    """
    if not isinstance(limit, int):
        raise TypeError("Limit must be an integer.")
    if not isinstance(offset, int):
        raise TypeError("Offset must be an integer.")
    if limit < 1 or offset < 1:
        raise ValueError("Limit and offset must be positive.")

    query = """
    SELECT title from movies
    LIMIT ? OFFSET ?
    """

    real_offset = (offset - 1) * limit if offset > 0 else 0
    with create_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(query, (limit, real_offset))
        movies = cursor.fetchall()
        if movies:
            for movie in movies:
                print(f"{movie[0]}")
        else:
            print("No movies found.")


def get_all_movies_and_actors():
    """
    Gets all movies and actors.
    """
    query = """
    SELECT TITLE FROM movies
    UNION 
    SELECT NAME FROM actors;
    """

    with create_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(query)
        result = cursor.fetchall()

        if result:
            for row in result:
                print(f"{row[0]}")
        else:
            print("No movies or actors found.")


def get_movies_with_age():
    """
    Gets all movies with their age.
    """
    query = """SELECT title, movie_age(release_year) AS age FROM movies"""

    with create_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(query)
        result = cursor.fetchall()

        if result:
            for row in result:
                print(f"{row[0]}: {row[1]} years")
        else:
            print("No movies found.")
