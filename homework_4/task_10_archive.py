import zipfile

class ArchiveContextManager:
    """
    Archive context manager.
    """

    def __init__(self, archive_name: str):
        """
        Constructor.
        :param archive_name: name of the archive
        """
        self.archive_name = archive_name
        self.zip = None

    def __enter__(self):
        """
        Loading manager while entering the context manager.
        :return: archive context manager
        """
        self.zip = zipfile.ZipFile(self.archive_name, mode='w', compression=zipfile.ZIP_DEFLATED)
        return self

    def add_file(self, filename: str):
        """
        Helper method to add a file to the archive.
        :param filename: the name of the file to add to the archive
        """
        self.zip.write(filename, arcname=filename)

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Closing the archive context manager.
        """
        if self.zip:
            self.zip.close()


if __name__ == '__main__':
    with ArchiveContextManager('data/test.zip') as archive:
        archive.add_file('data/task_10_1.txt')
        archive.add_file('data/task_10_2.txt')
        archive.add_file('data/task_10_3.txt')

    with zipfile.ZipFile('data/test.zip', 'r') as zf:
        print("Files in archive:", zf.namelist())