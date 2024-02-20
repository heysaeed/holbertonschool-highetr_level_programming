#!/usr/bin/python3
import unittest
from models.rectangle import Rectangle

"""Change order of attribute according to your own"""


class TestRectangle(unittest.TestCase):

    def test_rectangle_init(self):
        rectangle = Rectangle(3, 2)
        self.assertEqual(rectangle.width, 3)
        self.assertEqual(rectangle.height, 2)

    def test_rectangle_init_with_pos(self):
        rectangle = Rectangle(3, 2, 1)
        self.assertEqual(rectangle.x, 1)
        self.assertEqual(rectangle.y, 0)

    def test_rectangle_init_with_id(self):
        rectangle = Rectangle(3, 2, 1, 0, 10)
        self.assertEqual(rectangle.id, 10)

    def test_rectangle_int_error(self):
        with self.assertRaises(TypeError) as err:
            rectangle = Rectangle("hello", 2, 3)
        self.assertEqual(str(err.exception), "width must be an integer")

    def test_rectangle_value_error(self):
        with self.assertRaises(ValueError) as err:
            rectange = Rectangle(-2, 1)
        self.assertEqual(str(err.exception), "width must be > 0")

    def test_rectangle_area(self):
        rectangle = Rectangle(3, 2)
        self.assertEqual(rectangle.area(), 6)

    def test_rectangle_str(self):
        rectangle = Rectangle(3, 2, 1, 0, 10)
        expected_output = "[Rectangle] (10) 1/0 - 3/2"
        self.assertEqual(str(rectangle), expected_output)

    def test_rectangle_update(self):
        rectangle = Rectangle(3, 2, 1, 0, 10)
        rectangle.update(25, 30, 20, 0, 1)
        self.assertEqual(rectangle.width, 30)
        self.assertEqual(rectangle.height, 20)
        self.assertEqual(rectangle.x, 0)
        self.assertEqual(rectangle.y, 1)
        self.assertEqual(rectangle.id, 25)

    def test_rectangle_update_kwargs(self):
        rectangle = Rectangle(3, 2, 1, 0, 10)
        rectangle.update(height=10)
        self.assertEqual(rectangle.height, 10)

    def test_rectangle_to_dictionary(self):
        rectangle = Rectangle(3, 2, 1, 0, 10)
        rectangle_dict = rectangle.to_dictionary()
        expected_dict = {'id': 10, 'width': 3, 'height': 2, 'x': 1, 'y': 0}
        self.assertEqual(rectangle_dict, expected_dict)
