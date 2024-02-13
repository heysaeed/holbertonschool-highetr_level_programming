#!/usr/bin/python3
"""
Define function is_same_class
"""


def is_same_class(obj, a_class):
    """
    return True if object is exactly an instance
    of the specified class,otherwise false
    """
    return type(obj) is a_class
