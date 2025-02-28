"""
Module: parallel_image_processor
---------------------------------
This module provides functionality to process images in a folder using multiprocessing.
It resizes images to 200x200 pixels in parallel using the `concurrent.futures` module.
"""

import concurrent.futures
import os

from PIL import Image, UnidentifiedImageError


def image_editor(image_path: str) -> None:
    """
    Resizes an image to 200x200 pixels and saves it.
    :param image_path: The full path to the image file.
    :return: None
    :raises UnidentifiedImageError: If an unrecognized image is found.
    :raises FileNotFoundError: If an image file was not found.
    :raises TypeError: If an image file was not found.
    """
    if not isinstance(image_path, str):
        raise TypeError("image_path must be a string")

    if not os.path.isfile(image_path):
        print(f"Error: Folder '{image_path}' not found.")

    try:
        image = Image.open(image_path)
        image = image.resize((200, 200))
        image.save(image_path)
        print(f"Image {image_path} resized")
    except FileNotFoundError:
        print(f"File not found: {image_path}")
    except UnidentifiedImageError:
        print(f"Unsupported image: {image_path}")


def parallel_processor(folder_name: str) -> None:
    """
    Processes multiple images in a given folder using multiprocessing.
    It resizes images to 200x200 pixels in parallel.
    :param folder_name: The path to the folder containing images.
    :return: None
    :raises TypeError: If folder_name was not a string.
    """
    if not isinstance(folder_name, str):
        raise TypeError("folder_name must be a string")

    if not os.path.exists(folder_name):
        print(f"Error: Folder '{folder_name}' not found.")
        return

    extensions = (".jpg", ".jpeg", ".png", ".gif", ".bmp")
    images = [file for file in os.listdir(folder_name) if file.lower().endswith(extensions)]

    if len(images) == 0:
        print(f"No images found in '{folder_name}'")
        return

    with concurrent.futures.ProcessPoolExecutor() as executor:
        futures = [executor.submit(image_editor, os.path.join(folder_name, image)) for image in images]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occured: {e}")


if __name__ == "__main__":
    parallel_processor('task_2_test_images')
