#!/usr/bin/python3
"""JSON file loading module."""
import json


def load_from_json_file(filename):
    """Deserializes a JSON file to a Python object.

    Opens a file, reads the JSON string from it, and converts it into a Python object.

    Args:
        filename (str): The name of the file containing the JSON string.

    Returns:
        The Python object derived from the JSON string in the file.
    """
    with open(filename, "r") as file:
        return json.load(file)
