#!/usr/bin/python3
"""Module for the square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represents a square, inheriting from Rectangle."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square instance."""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """int: The size of the square's sides."""
        return self.width

    @size.setter
    def size(self, value):
        """Set square size, adjusting width and height."""
        self.width = value
        self.height = value

    def __str__(self):
        """Return string representation of a Square."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                 self.y, self.size)

    def update(self, *args, **kwargs):
        """Update Square attributes via args or kwargs.
        Attributes order: id, size, x, y.
        """
        attributes = ['id', 'size', 'x', 'y']
        if args and len(args) > 0:
            attributes_with_value = list(zip(attributes, args))
            for attr, arg in attributes_with_value:
                setattr(self, attr, arg)
        elif kwargs:
            for key, value in kwargs.items():
                if key in attributes:
                    setattr(self, key, value)

    def to_dictionary(self):
        """Return dictionary representation of a Square."""
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }
