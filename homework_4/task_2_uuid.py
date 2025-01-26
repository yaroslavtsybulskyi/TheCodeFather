import uuid


class UniqueIdIterator:
    """
    Class that iterates through a list of unique ids.
    """

    def __init__(self, count):
        """
        Constructor.
        :param count:
        """
        if not isinstance(count, int):
            raise TypeError('Count must be an integer')
        if count < 1:
            raise ValueError('Count must be >= 1')
        self._count = count
        self._generated = 0

    def __iter__(self):
        """Returns the iterator object."""
        return self

    def __next__(self) -> str:
        """Returns the next unique id."""
        if self._generated > self._count - 1:
            raise StopIteration

        self._generated += 1
        return str(uuid.uuid4())


if __name__ == '__main__':
    test = UniqueIdIterator(4)
    print(next(test))
    print(next(test))
    print(next(test))
    print(next(test))
    print(next(test))
