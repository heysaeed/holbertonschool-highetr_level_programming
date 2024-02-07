#!/usr/bin/python3
"""
Define a Rectangle class
"""


class Rectangle:
    """Define the rectangle attribute"""
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """
        initialisation of the rectangle
        incrementation of number_of_instances
        Args:
            width (int, optional): width of the rectangle. Defaults to 0.
            height (int, optional): height of the rectangle. Defaults to 0.
        """
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        Returns:
            int: width of the rectangle
        """
        return self.__width

    @property
    def height(self):
        """
        Returns:
            int: height of the rectangle
        """
        return self.__height

    @width.setter
    def width(self, value):
        """Setter of width

        Args:
            value (int): width of rectangle to set

        Raises:
            TypeError: width must be an integer
            ValueError: width must be >= 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """Setter of height

        Args:
            value (int): height of rectangle to set

        Raises:
            TypeError: height must be an integer
            ValueError: height must be >= 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculate the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculate the perimeter of the rectangle.

        Returns:
            int: The perimeter of the rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        """
        Return the rectangle as #.
        Return an empty string if either width or height is 0.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        rectangle_print = (str(self.print_symbol) * self.__width + '\n') * \
            (self.__height - 1) + (str(self.print_symbol) * self.__width)
        return rectangle_print

    def __repr__(self):
        """

        Returns:
            str: string representation of a rectangle
        """
        return ("Rectangle({}, {})".format(self.__width, self.__height))

    def __del__(self):
        """
        Decrease number_of_instances for each deletion
        print string if object is deleted
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Compare two rectangle to check which one is
        bigger

        Args:
            rect_1 (Rectangle): first rectangle to compare
            rect_2 (Rectangle): second rectangle to compare

        Raises:
            TypeError: Rect_1 must be a Rectangle
            TypeError: Rect_2 must be a Rectangle

        Returns:
            Rectangle: bigger rectangle or rect_1 if equals
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """class method to return a square

        Args:
            size (int, optional): size of the square. Defaults to 0.

        Returns:
            Rectangle: a new square
        """
        return cls(size, size)
