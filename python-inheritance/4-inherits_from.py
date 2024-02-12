#!/usr/bin/python3


def inherits_from(obj, a_class):
    """ return True if object is an instance of a class that inherited
    (directly or indirectly) from the specified class,otherwise false"""
    return (type(obj) != a_class and isinstance(obj, a_class))
