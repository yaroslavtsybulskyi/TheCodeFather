import json


def load_books(filename: str):
    """
    The function loads books from a json file
    :param filename: the name of the json file
    """
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            books = json.load(f)
            return books
    except FileNotFoundError:
        print(f'File {filename} not found.')
        return []
    except json.decoder.JSONDecodeError:
        print(f'File {filename} could not be decoded.')
        return []


def get_available_books_only(filename: str) -> None:
    """
    The function gets all books available on a json file
    :param filename: the filename of the json file
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


def save_book(filename: str, data: list) -> None:
    """
    The function saves a book into a json file
    :param filename: the name of the json file to save the value
    :param data: the book value to save
    """
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f'Error: {e}')


def add_book(filename: str, book: dict) -> None:
    """
    The function adds a book into a json file
    :param filename: the name of the json file to save the value
    :param book: the book value to save
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
