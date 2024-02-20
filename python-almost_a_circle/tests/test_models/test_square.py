#!/usr/bin/python3
import unittest
from models.square import Square

"""Change order of attribute according to your own"""

class TestSquare(unittest.TestCase):

    def test_square_init(self):
        square = Square(3)
        self.assertEqual(square.size, 3)

    def test_square_init_with_pos(self):
        square = Square(3, 2, 1)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 1)

    def test_square_init_with_id(self):
        square = Square(3, 2, 1, 10)
        self.assertEqual(square.id, 10)

    def test_square_int_error(self):
        with self.assertRaises(TypeError) as err:
            square = Square("hello", 2, 3)
        self.assertEqual(str(err.exception), "width must be an integer")

    def test_square_value_error(self):
        with self.assertRaises(ValueError) as err:
            square = Square(-2)
        self.assertEqual(str(err.exception), "width must be > 0")

    def test_square_area(self):
        square = Square(3)
        self.assertEqual(square.area(), 9)

    def test_square_str(self):
        square = Square(3, 2, 1, 10)
        expected_output = "[Square] (10) 2/1 - 3"
        self.assertEqual(str(square), expected_output)

    def test_square_update(self):
        square = Square(3, 2, 1, 10)
        square.update(25, 30, 20, 10)
        self.assertEqual(square.size, 30)
        self.assertEqual(square.x, 20)
        self.assertEqual(square.y, 10)
        self.assertEqual(square.id, 25)

    def test_square_update_kwargs(self):
        square = Square(3, 2, 1, 10)
        square.update(size=10)
        self.assertEqual(square.size, 10)

    def test_square_to_dictionary(self):
        square = Square(3, 2, 1, 10)
        square_dict = square.to_dictionary()
        expected_dict = {'id': 10, 'size': 3, 'x': 2, 'y': 1}
        self.assertEqual(square_dict, expected_dict)