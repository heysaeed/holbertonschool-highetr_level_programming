#!/usr/bin/python3
def lookup(obj):
    """return the list of available attributes and methods of an object

    Args:
        obj : object to list available attributes
    Returns:
        list: attributes
    """
    return dir(obj)
