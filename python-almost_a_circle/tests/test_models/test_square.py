#!/usr/bin/python3
import unittest
import json
import os
from models.square import Square


class TestSquare(unittest.TestCase):

    def test_square_init(self):
        square = Square(3)
        self.assertEqual(square.size, 3)
        square = Square(3, 1)
        self.assertEqual(square.x, 1)

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
        with self.assertRaises(TypeError) as err:
            square = Square(1, "2", 3)
        self.assertEqual(str(err.exception), "x must be an integer")
        with self.assertRaises(TypeError) as err:
            square = Square(1, 2, "3")
        self.assertEqual(str(err.exception), "y must be an integer")

    def test_square_value_error(self):
        with self.assertRaises(ValueError) as err:
            square = Square(-2)
        self.assertEqual(str(err.exception), "width must be > 0")
        with self.assertRaises(ValueError) as err:
            square = Square(2, -2)
        self.assertEqual(str(err.exception), "x must be >= 0")
        with self.assertRaises(ValueError) as err:
            square = Square(1, 2, -2)
        self.assertEqual(str(err.exception), "y must be >= 0")
        with self.assertRaises(ValueError) as err:
            square = Square(0)
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

    def test_square_create_id(self):
        square = Square.create(**{ 'id': 89})
        self.assertEqual(square.id, 89)

    def test_square_create_id_size(self):
        square = Square.create(**{ 'id': 89, 'size': 1})
        self.assertEqual(square.id, 89)
        self.assertEqual(square.size, 1)

    def test_square_create_id(self):
        square = Square.create(**{ 'id': 89, 'size': 1, 'x': 2})
        self.assertEqual(square.id, 89)
        self.assertEqual(square.size, 1)
        self.assertEqual(square.x, 2)

    def test_square_create_id(self):
        square = Square.create(**{ 'id': 89, 'size': 1, 'x': 2, 'y': 3 })
        self.assertEqual(square.id, 89)
        self.assertEqual(square.size, 1)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)

    def setUp(self):
        self.filename = "Square.json"

    def tearDown(self):
        if os.path.exists(self.filename):
            os.remove(self.filename)

    def test_square_save_to_file_none(self):
        Square.save_to_file(None)
        self.assertTrue(os.path.exists(self.filename))
        with open(self.filename, 'r') as file:
            file_read = file.read()
            self.assertEqual(file_read, "[]")

    def test_square_save_to_file_empty(self):
        Square.save_to_file([])
        self.assertTrue(os.path.exists(self.filename))
        with open(self.filename, 'r') as file:
            file_read = file.read()
            self.assertEqual(file_read, "[]")

    def test_square_save_to_file(self):
        square = Square(1)
        Square.save_to_file([square])
        self.assertTrue(os.path.exists(self.filename))
        with open(self.filename, 'r') as file:
            file_read = file.read()
            expected_content = json.dumps([square.to_dictionary()])
            self.assertEqual(json.loads(file_read), json.loads(expected_content))

    @classmethod
    def setUpClass(cls):
        cls.filename = "Rectangle.json"

    @classmethod
    def tearDownClass(cls):
        if os.path.exists(cls.filename):
            os.remove(cls.filename)

    def test_square_load_from_file_nofile(self):
        if os.path.exists(self.filename):
            os.remove(self.filename)
        result = Square.load_from_file()
        self.assertEqual(result, [])

    def test_rectangle_load_from_file(self):
        squares = [
            {"id": 1, "size": 2, "x": 2, "y": 3},
            {"id": 2, "size": 3, "x": 0, "y": 0},
        ]
        with open(self.filename, "w") as file:
            file.write(Square.to_json_string(squares))
        loaded_file = Square.load_from_file()
        self.assertTrue(len(loaded_file) == len(squares))
        for loaded_square, expected_square in zip(loaded_file, squares):
            self.assertTrue(isinstance(loaded_square,Square))
            for key in expected_square:
                self.assertEqual(getattr(loaded_square,key), expected_square[key])