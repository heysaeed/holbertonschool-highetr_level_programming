#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""define a Rectangle"""


class Rectangle(BaseGeometry):
    """define Rectangle attribute

    Args:
        BaseGeometry (class)
    """
    def __init__(self, width, height):
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