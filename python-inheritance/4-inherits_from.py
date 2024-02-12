#!/usr/bin/python3
""" return True if object is exactly an instance
of the specified class,otherwise false	"""


def inherits_from(obj, a_class):
    return (type(obj) != a_class and isinstance(obj, a_class))
