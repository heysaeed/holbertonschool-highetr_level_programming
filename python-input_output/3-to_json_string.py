#!/usr/bin/python3
"""JSON serialization module."""
import json


def to_json_string(my_obj):
    """Converts an object to a JSON string.

    Args:
        my_obj: The object to serialize.

    Returns:
        str: JSON representation of `my_obj`.
    """
    file = json.dumps(my_obj)
    return file
