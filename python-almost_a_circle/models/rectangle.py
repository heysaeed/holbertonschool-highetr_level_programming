#!/usr/bin/python3
"""module for the rectangle class"""
from models.base import Base


class Rectangle(Base):
    """A class representing a rectangle, inheriting from Base."""
    print_symbol = "#"

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle instance."""
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
            int: x position of the rectangle
        """
        return self.__x

    @property
    def y(self):
        """
        Returns:
            int: y position of the rectangle
        """
        return self.__y

    @width.setter
    def width(self, value):
        """Set width after validating it's an int > 0."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """Set height after validating it's an int > 0."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """Set x after validating it's an int >= 0."""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """Set y after validating it's an int >= 0."""
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
        """Prints the rectangle using `#` as symbol."""
        if self.__y > 0:
            print('\n' * self.__y, end='')
        print(((' ' * self.__x) + str(self.print_symbol) * self.__width +
              '\n') * (self.__height - 1) + ((' ' * self.__x)
                                             + str(self.print_symbol)
                                             * self.__width))

    def __str__(self):
        """String representation of the Rectangle."""
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x,
                                                        self.__y, self.__width,
                                                        self.__height))

    def update(self, *args, **kwargs):
        """Updates the rectangle's attributes with args or kwargs."""
        attributes = ['id', 'width', 'height', 'x', 'y']
        if args and len(args) > 0:
            attributes_with_value = list(zip(attributes, args))
            for attr, arg in attributes_with_value:
                setattr(self, attr, arg)
        elif kwargs:
            for key, value in kwargs.items():
                if key in attributes:
                    setattr(self, key, value)

    def to_dictionary(self):
        """Dictionary representation of a Rectangle's attributes."""
        return {
            'id': self.id,
            'width': self.__width,
            'height': self.__height,
            'x': self.__x,
            'y': self.__y
        }
