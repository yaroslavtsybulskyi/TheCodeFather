"""
Movie Database Console Application
This module provides a command-line interface for managing a movie database.
"""

from homework_10.db import create_tables
from homework_10.models import add_movie, add_actor
from homework_10.queries import get_movies_with_actors, get_unique_genres, get_movie_count_by_genre, \
    get_average_age_by_genre, search_movies_with_like, get_movies_with_limit, get_all_movies_and_actors, \
    get_movies_with_age


def main():
    """
    Runs the Movie Database console application.
    """
    create_tables()

    while True:
        print('Menu')
        print('1 - Add Movie')
        print('2 - Add Actor')
        print('3 - Show All Movies with Actors')
        print('4 - Show Unique Genres')
        print('5 - Quantity of Movies within Genre')
        print('6 - Show Average Birth Year of Actor from Genre')
        print('7 - Find Movie by Name')
        print('8 - Show Movies with Pagination')
        print('9 - All Movies and Actors')
        print('10 - Check Movies Age')
        print('11 - Esc')

        try:
            choice = input('Enter your choice: ')
            match choice:
                case '1':
                    title = input('Enter movie title: ')
                    release_year = int(input('Enter release year: '))
                    genre = input('Enter genre: ')
                    actors = input('Enter actors (separate by comma): ').split(", ")
                    add_movie(title, release_year, genre, actors)
                    print(f"Movie {title} added.")
                case '2':
                    name = input('Enter actor name: ')
                    birth_year = int(input('Enter birth year: '))
                    add_actor(name, birth_year)
                    print(f"Actor {name} added.")
                case '3':
                    get_movies_with_actors()
                case '4':
                    get_unique_genres()
                case '5':
                    get_movie_count_by_genre()
                case '6':
                    genre = input('Enter movie genre: ')
                    get_average_age_by_genre(genre)
                case '7':
                    name = input('Enter movie name (or part of it): ')
                    search_movies_with_like(name)
                case '8':
                    limit = int(input('Enter number of movies per page: '))
                    offset = int(input('Enter number of page to show: '))
                    get_movies_with_limit(limit, offset)
                case '9':
                    get_all_movies_and_actors()
                case '10':
                    get_movies_with_age()
                case '11':
                    print('Goodbye!')
                    break
                case _:
                    print('Invalid choice, please, try again :) ')
        except Exception as e:
            print(f"An error occurred: {e}")


if __name__ == '__main__':
    main()
