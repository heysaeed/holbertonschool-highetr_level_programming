#!/usr/bin/python3
"""Module for BaseGeometry class."""


class BaseGeometry:
    """A base class for geometry objects."""

    def area(self):
        """
        Calculate the area of the geometry.
        Returns:
            int: The area of the geometry.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """check if value is int
        Args:
                name (str): name of the value
                value (int): value
        Raises:
                TypeError: if value is not an integer
                ValueError: if value is not more than 0
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
