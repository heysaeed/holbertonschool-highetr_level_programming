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
