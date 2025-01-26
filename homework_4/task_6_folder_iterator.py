import os


class FolderIterator:
    """Class to iterate over a folder structure"""

    def __init__(self, folder: str):
        """
        Constructor
        :param folder: address of the folder
        """
        self.folder = folder
        self.files = [os.path.join(self.folder, file) for file in os.listdir(self.folder)]
        self.index = 0

    def __iter__(self):
        """Returns the iterator object."""
        return self

    def __next__(self):
        """Returns the next item from the iterator."""
        if self.index >= len(self.files):
            raise StopIteration

        file = self.files[self.index]
        file_size = os.path.getsize(file)
        filename = os.path.basename(file)

        self.index += 1
        return f"{filename}: {file_size} bytes"


if __name__ == "__main__":
    current_directory = os.getcwd()
    test_folder = FolderIterator(current_directory)
    print(next(test_folder))
    print(next(test_folder))
