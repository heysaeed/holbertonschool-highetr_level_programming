#!/usr/bin/python3
from models.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.size)

    def update(self, *args, **kwargs):
        attributes = ['id', 'size', 'x', 'y']
        if args and len(args) > 0:
            attributes_with_value = list(zip(attributes, args))
            for attr, arg in attributes_with_value:
                setattr(self, attr, arg)
        elif kwargs:
            for key, value in kwargs.items():
                if key in attributes:
                    setattr(self, key, value)
