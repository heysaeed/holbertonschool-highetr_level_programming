#!/usr/bin/python3
"""
Module defines a Square class with attributes and methods to manipulate
square properties.
"""


class Square:

    """
    A class that represents a square.

    Attributes:
        __size (int): The size of a side of the square.
        __position (tuple of int): The x, y position of the square when
        printed.

    Methods:
        __init__(self, size=0, position=(0, 0)): Initializes a new
        Square.
        area(self): Calculates the area of the square.
        size(self): Gets the current square size.
        size(self, value): Sets the size of the square.
        my_print(self): Prints the square with the character '#'.
        position(self): Gets the current position.
        position(self, value): Sets the position of the square.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize a new Square instance.

        Args:
            size (int, optional): The size of the square's side.
            Defaults to 0.
            position (tuple of int, optional): The x, y coordinates where
            the square will be printed. Defaults to (0, 0).

        Raises:
            TypeError: If 'size' is not an integer.
            ValueError: If 'size' is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        self.position = position

    def area(self):
        """
        Calculate the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    @property
    def size(self):
        """
        Get the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If 'value' is not an integer.
            ValueError: If 'value' is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """
        Print the square with the character '#' to the console, using the
        position attribute to offset it.
        """
        if self.__size == 0:
            print()
        else:
            print("\n" * self.__position[1], end="")
            for x in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)

    @property
    def position(self):
        """
        Get the position of the square.

        Returns:
            tuple of int: The position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Set the position of the square.

        Args:
            value (tuple of int): The new position of the square.

        Raises:
            TypeError: If 'value' is not a tuple of 2 positive integers.
        """
        if not (isinstance(value, tuple) and len(value) == 2
                and all(isinstance(x, int) and x >= 0 for x in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
