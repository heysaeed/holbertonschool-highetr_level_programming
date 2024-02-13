#!/usr/bin/python3
"""Module for file writing operations. appending if needed"""


def append_write(filename="", text=""):
    """Appends text to a file, returns the number of characters added.

    Opens a file in append mode or creates it. Writes `text` to the file, then
    returns the count of characters written.

    Args:
        filename (str, optional): Path to the file. Defaults to "".
        text (str, optional): Text to append. Defaults to "".

    Returns:
        int: Number of characters written.
    """
    with open(filename, "a") as file:
        return file.write(text)
