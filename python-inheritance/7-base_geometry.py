#!/usr/bin/python3
"""define a base geometry"""


class BaseGeometry:

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
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
