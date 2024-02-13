#!/usr/bin/python3
"""JSON file saving module."""
import json


def save_to_json_file(my_obj, filename):
    """Serializes an object to a JSON string and writes it to a file.

    Args:
        my_obj: The Python object to serialize.
        filename (str): The name of the file where the JSON string
        will be saved.

    """
    with open(filename, "w") as newfile:
        content = json.dumps(my_obj)
        newfile.write(content)
