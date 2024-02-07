#!/usr/bin/python3

"""
Module for addition
"""


def add_integer(a, b=98):
    """add two integers

    Args:
            a (int): first int
            b (int, optional): second int. Defaults to 98.

    Returns:
            int: sum
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
