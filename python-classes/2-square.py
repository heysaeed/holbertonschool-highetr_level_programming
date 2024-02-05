#!/usr/bin/python3
"""
Define a square class
"""


class Square:
    """
    define attribute of square
    """

    def __init__(self, size=0):
        """
        initialize a square
        Args:
            size (int, optional): _description_. Defaults to 0.
        Raises:
                TypeError: size must be an integer
                ValueError: size must be >=0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
