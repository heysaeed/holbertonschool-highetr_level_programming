#!/usr/bin/python3
"""define a base geometry"""


class BaseGeometry:
    """define base geometry attributes
    """

    def area(self):
        """
        Calculate the area of the geometry.

        Returns:
            int: The area of the geometry.
        """
        raise Exception("area() is not implemented")
