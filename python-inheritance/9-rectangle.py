#!/usr/bin/python3
"""Module for Rectangle class."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A class that represents a rectangle, inheriting from BaseGeometry.

    Attributes:
        width (int): The width of the rectangle, must be a positive integer.
        height (int): The height of the rectangle, must be a positive integer.
    """

    def __init__(self, width, height):
        """Initializes a new Rectangle instance.
        Args:
            width (int): The width of rectangle, must be positive integer.
            height (int): The height of rectangle, must be positive integer.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """
        Calculate the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Returns:
            str: [Rectangle] <width>/<height>
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
