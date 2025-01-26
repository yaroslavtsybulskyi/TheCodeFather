def endless_even_number_generator():
    """
    Generator that yields even numbers endlessly.
    :return: yields even numbers.
    """
    number = 0
    while True:
        yield number
        number += 2


class ContextManagerForEvenNumberGenerator:
    """
    Context manager that yields even numbers endlessly or until the limit is reached.
    """

    def __init__(self, filename, limit=20) -> None:
        """
        Constructor.
        :param filename: the name of the file to open for writing.
        :param limit: the maximum number of even numbers to yield.
        """
        self.file = None
        self.filename = filename
        self.limit = limit
        self.generator = endless_even_number_generator()

    def __enter__(self):
        """
        Enter to the context manager.
        """
        self.file = open(self.filename, 'w', encoding='UTF-8')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Exit from the context manager.
        """
        if self.file:
            self.file.close()

    def write_file(self):
        """Helper method to write the data to the file."""
        for _ in range(self.limit):
            self.file.write(f"{next(self.generator)}\n")


if __name__ == '__main__':
    with ContextManagerForEvenNumberGenerator('data/task_5.txt') as file:
        file.write_file()
