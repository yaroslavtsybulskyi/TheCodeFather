"""
Module: parallel_image_processor
---------------------------------
This module provides functionality to process images in a folder using multiprocessing.
It resizes images to 200x200 pixels in parallel using the `concurrent.futures` module.
"""

import concurrent.futures
import os
import logging
from pathlib import Path

from PIL import Image, UnidentifiedImageError

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


def image_editor(image_path: str) -> None:
    """
    Resizes an image to 200x200 pixels and saves it.
    :param image_path: The full path to the image file.
    :return: None
    :raises UnidentifiedImageError: If an unrecognized image is found.
    :raises TypeError: If an image file was not found.
    :raises OSError: If an error occurs during file processing (e.g., permission issues, corrupt file).
    """
    if not isinstance(image_path, str):
        raise TypeError("image_path must be a string")

    if not os.path.isfile(image_path):
        logging.error("Error: File '%s' not found.", image_path)
        return

    try:
        image = Image.open(image_path)
        image = image.resize((200, 200))

        original_path = Path(image_path)
        resized_filename = f"{original_path.stem}_resized{original_path.suffix}"
        resized_filepath = original_path.parent / resized_filename
        try:
            image.save(resized_filepath)
        except OSError as e:
            logging.error("Failed to save image %s: %s", resized_filename, e)
            return
        logging.info("Image %s resized successfully", image_path)
    except UnidentifiedImageError:
        logging.error("Unsupported image format: %s", image_path)
    except Exception as e:
        logging.error("Unexpected error processing %s: %s", image_path, e)


def parallel_processor(folder_name: str, max_workers: int = 4) -> None:
    """
    Processes multiple images in a given folder using multiprocessing.
    It resizes images to 200x200 pixels in parallel.
    :param folder_name: The path to the folder containing images.
    :param max_workers: The maximum number of concurrent processes. Defaults to 4.
    :return: None
    :raises TypeError: If folder_name was not a string or max_workers was not a int.
    :raises RuntimeError: If an unexpected runtime error occurs during processing.
    """
    if not isinstance(folder_name, str):
        raise TypeError("Folder_name must be a string")

    if not os.path.exists(folder_name):
        logging.error("Error: Folder '%s' not found.", folder_name)
        return

    if not isinstance(max_workers, int):
        raise TypeError("max_workers must be an integer")

    extensions = (".jpg", ".jpeg", ".png", ".gif", ".bmp")
    images = [file for file in os.listdir(folder_name) if file.lower().endswith(extensions)]

    if len(images) == 0:
        logging.warning("No images found in '%s'", folder_name)
        return

    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {executor.submit(image_editor,
                                   os.path.join(folder_name, image)): image for image in images}
        for future in concurrent.futures.as_completed(futures):
            image_path = futures[future]
            try:
                future.result()
            except RuntimeError as e:
                logging.error("Runtime error while processing '%s': %s", image_path, e)
            except Exception as e:
                logging.error("Error occurred while processing '%s': %s", image_path, e)


if __name__ == "__main__":
    parallel_processor('task_2_test_images')
