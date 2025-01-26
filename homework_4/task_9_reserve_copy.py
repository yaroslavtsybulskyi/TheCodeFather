import os
import shutil


class ReserveCopyManager:
    """
    ReserveCopyManager is saving the copy of the file and restoring file in case of failure.
    """

    def __init__(self, filename: str) -> None:
        """
        constructor
        :param filename: filename
        """
        self.filename = filename
        self.copy = f"{filename}.copy"

    def __enter__(self):
        """
        Loading manager while entering context
        :return: returns self.filename
        """
        if not os.path.exists(self.filename):
            raise FileNotFoundError(f"File {self.filename} does not exist")

        shutil.copy2(self.filename, self.copy)
        print(f"Copied {self.filename} to {self.copy}")
        return self.filename

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Restoring file or removing copy in case of failure on exit context
        """
        if exc_type is None:
            os.remove(self.copy)
            print(f"Removed {self.copy}")
        else:
            shutil.copy2(self.copy, self.filename)
            os.remove(self.copy)
            print(f"Copied {self.copy} to {self.filename}")


if __name__ == "__main__":
    with ReserveCopyManager("data/task_9_test_file.txt") as file:
        with open(file, 'a', encoding='UTF-8') as filename:
            filename.write("Hello World")
            raise Exception("test")
