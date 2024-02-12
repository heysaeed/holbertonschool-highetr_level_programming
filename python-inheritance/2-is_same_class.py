#!/usr/bin/python3
""" return True if object is exactly an instance
of the specified class,otherwise false	"""


def is_same_class(obj, a_class):
    if isinstance(obj, a_class):
        return True
    else:
        return False
