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
