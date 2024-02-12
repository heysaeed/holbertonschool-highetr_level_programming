#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle
"""Define the Square class
"""


class Square(Rectangle):
    """define Square attribute

        Args:
                Rectangle (class)
        """

    def __init__(self, size):
        """initiate a Square

            Args:
                    size (int): size of the square
        """
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """
        Calculate the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2