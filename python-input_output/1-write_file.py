#!/usr/bin/python3
"""Module for file writing operations."""


def write_file(filename="", text=""):
    """write a file
    (create one if none exist)

        Args:
                filename (str, optional): name of the file to
                write into. Defaults to "".
                text (str, optional): text to write into file.
                Defaults to "".

        Returns:
                int: number of char written
        """
    with open(filename, "w") as file:
        return file.write(text)
