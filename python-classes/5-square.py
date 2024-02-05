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
            size (int, optional): size of the square. Defaults to 0.
        Raises:
                TypeError: size must be an integer
                ValueError: size must be >=0
        """
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

    @property
    def size(self):
        """
        Returns:
            int: size of square
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """
        Args:
                value (int): size of square
        Raises:
                TypeError: size must be an integer
                ValueError: size must be >=0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """
        print a square of self.__size with #
        """
        if self.__size:
            for x in range(self.__size):
                for y in range(self.__size):
                    print("#", end="")
                print()
        else:
            print()
