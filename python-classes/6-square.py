#!/usr/bin/python3
"""
Define a square class
"""


class Square:
    """
    define attribute of square
    """

    def __init__(self, size=0, position=(0, 0)):
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
        self.__position = position

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
        if self.__size == 0:
            print()
        else:
            for space in range(self.__position[1]):
                print()
            for x in range(self.__size):
                for space in range(self.__position[0]):
                    print(" ", end="")
                for y in range(self.__size):
                    print("#", end="")
                print()

    @property
    def position(self):
        """
        Returns:
            tuple(int): position the square should be printed on output
        """
        return self.__position

    @position.setter
    def position(self, value):
        if not (isinstance(value, tuple) and len(value) == 2
                and all(isinstance(x, int) and x >= 0 for x in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
