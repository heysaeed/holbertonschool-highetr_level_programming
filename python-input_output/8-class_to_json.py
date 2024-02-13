#!/usr/bin/python3
"""Object to JSON conversion module."""


def class_to_json(obj):
    """Converts object's attributes to a dictionary for JSON serialization.

    This function takes an object as input and returns its `__dict__` attribute,
    which contains all its fields in a dictionary format. This is useful for
    serializing custom class instances to JSON.

    Args:
        obj: The object to be converted.

    Returns:
        A dictionary representation of the object's attributes.
    """
    return obj.__dict__
