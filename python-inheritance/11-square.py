#!/usr/bin/python3
"""Module for Square class."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class that represents a square, inheriting from Rectangle.
    Attributes:
        size (int): The size of the square's sides, must be a
        positive integer.
    """

    def __init__(self, size):
        """Initializes a new Square instance.

        Validates the size using the parent class (Rectangle)'s
        integer_validator
        method and then calls the Rectangle's constructor with size
        as both the width and height.

        Args:
            size (int): The size of the square's sides.
            Must be a positive integer.
        """
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """Calculates the area of the square.

        Overrides the area method from Rectangle to use the square's size.

        Returns:
            The area of the square.
        """
        return self.__size ** 2

    def __str__(self):
        """Provides a string representation of the Square instance.

        Overrides the object's default method to return the square's description,
        including its size.

        Returns:
            str: A string in the format "[Square] size/size".
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
