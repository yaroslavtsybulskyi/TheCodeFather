import csv
import os

from PIL import Image


class ImageMetadataIterator:
    """
    Image metadata iterator.
    """

    def __init__(self, folder: str):
        """
        Constructor.
        :param folder: folder to iterate over.
        """
        self.folder = folder
        self.images = [file for file in os.listdir(self.folder)
                       if file.lower().endswith((".jpg", ".png", ".jpeg"))]
        self._index = 0
        self._headers = False

    def _open_image(self, index: int):
        """
        Helper method to open an image.
        :param index: index of the image in the folder
        :return: returns image
        """
        return Image.open(os.path.join(self.folder, self.images[index]))

    def _save_metadata_to_csv(self, metadata):
        """
        helper method to save metadata to CSV.
        :param metadata: metadata to save
        """
        with open('data/metadata.csv', 'a', newline='', encoding='UTF-8') as csvfile:
            fieldnames = ['filename', 'width', 'height', 'filesize', 'format']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            if not self._headers:
                writer.writeheader()
                self._headers = True
            writer.writerow(metadata)

    def __iter__(self):
        """Returns the iterator object."""
        return self

    def __next__(self):
        """
        Returns the next image from the iterator.
        :return: metadata about image
        """
        if self._index > len(self.images) - 1:
            raise StopIteration

        image = self._open_image(self._index)

        metadata = {'filename': image.filename,
                    'width': image.width,
                    'height': image.height,
                    'filesize': image.size,
                    'format': image.format}

        self._index += 1
        self._save_metadata_to_csv(metadata)
        return metadata


if __name__ == '__main__':
    images = ImageMetadataIterator('/Users/yaroslavtsybulskyi/Downloads/Megathrone')
    next(images)
    next(images)
    next(images)
