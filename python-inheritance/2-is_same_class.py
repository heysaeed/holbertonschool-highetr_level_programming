#!/usr/bin/python3


def is_same_class(obj, a_class):
    """ return True if object is exactly an instance
    of the specified class,otherwise false	"""
    return type(obj) is not a_class
