#!/usr/bin/python3
from models.base import Base


class Rectangle(Base):
    print_symbol = "#"

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

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

    @property
    def x(self):
        """
        Returns:
            int: height of the rectangle
        """
        return self.__x

    @property
    def y(self):
        """
        Returns:
            int: height of the rectangle
        """
        return self.__y

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Calculate the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height

    def display(self):
        print((str(self.print_symbol) * self.__width + '\n') *
              (self.__height - 1) + (str(self.print_symbol) * self.__width))
