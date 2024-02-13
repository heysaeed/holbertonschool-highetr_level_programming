#!/usr/bin/python3
"""JSON deserialization module."""
import json


def from_json_string(my_str):
    """Converts a JSON string to a Python object.

    Args:
        my_str (str): JSON string to be deserialized.

    Returns:
        object: The Python object represented by `my_str`.
    """
    file = json.loads(my_str)
    return file
