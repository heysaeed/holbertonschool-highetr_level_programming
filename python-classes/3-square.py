#!/usr/bin/python3
"""
Define a square class
"""


class Square:
    """
    define attribute of square
    """

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Returns:
            int: return square of size
        """
        return self.__size * self.__size
