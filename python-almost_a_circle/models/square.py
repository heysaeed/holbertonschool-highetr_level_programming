#!/usr/bin/python3
from models.rectangle import Rectangle

class Square(Rectangle):
	def __init__(self, size, x=0, y=0, id=None):
		super().__init__(size, size, x, y, id)

	@property
	def size(self):
		return self.width
	
	def __str__(self):
		return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.size)