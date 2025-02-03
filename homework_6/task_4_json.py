import json
from typing import List, Dict


def load_books(filename: str) -> List[Dict]:
    """
    Load books from a JSON file.
    :param filename: The name of the JSON file to load the books from.
    :return: A list of books (as dictionaries).
    :raises FileNotFoundError: If the file is not found.
    :raises JSONDecodeError: If the file cannot be decoded.
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            books = json.load(file)
            return books
    except FileNotFoundError:
        print(f'File {filename} not found.')
        return []
    except json.decoder.JSONDecodeError:
        print(f'File {filename} could not be decoded.')
        return []


def get_available_books_only(filename: str) -> None:
    """
    Prints all available books from a JSON file.
    :param filename: The name of the JSON file to load books from.
    """
    books = load_books(filename)
    if not books:
        print("There are no books")
        return
    available_books = [book for book in books if book['available']]
    if not available_books:
        print("There are no available books")
        return
    for book in available_books:
        print(f"{book['title']} by {book['author']}")


def save_book(filename: str, data: List[Dict]) -> None:
    """
    Save a list of books to a JSON file.
    :param filename: The name of the JSON file to save the books to.
    :param data: The list of books to save.
    """
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f'Error: {e}')


def add_book(filename: str, book: Dict) -> None:
    """
    Add a book to a JSON file.
    :param filename: The name of the JSON file to save the book into.
    :param book: The book (as a dictionary) to add to the file.
    """
    books = load_books(filename)
    books.append(book)
    save_book(filename, books)


if __name__ == '__main__':
    print(load_books('data/books.json'))
    get_available_books_only('data/books.json')

    new_book = {"title": "Book 3", "author": "Author 3", "year": 2019, "available": True}
    add_book('data/books.json', new_book)
    get_available_books_only('data/books.json')
