#!/usr/bin/python3
"""
Define function ingerits_from
"""


def inherits_from(obj, a_class):
    """ return True if object is an instance of a class that inherited
    (directly or indirectly) from the specified class,otherwise false"""
    return (type(obj) is not a_class and isinstance(obj, a_class))
