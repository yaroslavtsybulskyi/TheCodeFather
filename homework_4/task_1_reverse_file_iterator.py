import os


class ReverseFileIterator:
    """
    Class Iterator that return line by line from the file in the reverse order
    """

    def __init__(self, filename: str) -> None:
        """
        Constructor
        :param filename: path of the file
        """
        self.filename = filename
        self._lines = self._read_file()
        self._index = len(self._lines) - 1

    def _read_file(self):
        """
        Reads the file
        :return: the lines of the file
        """
        with open(os.path.join(self.filename), 'r') as f:
            return f.readlines()

    def __iter__(self):
        """Returns the iterator object."""
        return self

    def __next__(self) -> str:
        """
        Returns the next line from the file
        :return: the next line
        """
        if self._index < 0:
            raise StopIteration

        line = self._lines[self._index]
        self._index -= 1
        return line.strip()


if __name__ == '__main__':
    my_file = ReverseFileIterator('data/file_for_task_1.txt')
    print(next(my_file))
    print(next(my_file))
    print(next(my_file))
    print(next(my_file))
    print(next(my_file))
    print(next(my_file))
    print(next(my_file))
    print(next(my_file))
    print(next(my_file))
    print(next(my_file))
