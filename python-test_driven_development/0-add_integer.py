#!/usr/bin/python3

"""
Module for addition
Add two integers
Cast float into ints
"""


def add_integer(a, b=98):
    """add two integers
    Returns: sum (int)
    """
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    if not (isinstance(a, int)):
        raise TypeError("a must be an integer")
    if not (isinstance(b, int)):
        raise TypeError("b must be an integer")
    return a + b
