#!/usr/bin/python3
"""print my name"""


def say_my_name(first_name, last_name=""):
    """say My name is first_name last_name

    Args:
            first_name (str): explicit
            last_name (str, optional): explicit. Defaults to "".

    Raises:
            TypeError: Need to be a str
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
