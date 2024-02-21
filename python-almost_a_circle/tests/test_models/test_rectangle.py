#!/usr/bin/python3
import unittest
import json
import sys
import os
from io import StringIO
from models.rectangle import Rectangle



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
        with self.assertRaises(TypeError) as err1:
            rectangle1 = Rectangle(1, "howdy", 3)
        self.assertEqual(str(err1.exception), "height must be an integer")
        with self.assertRaises(TypeError) as err2:
            rectangle1 = Rectangle(1, 2, "hi")
        self.assertEqual(str(err2.exception), "x must be an integer")
        with self.assertRaises(TypeError) as err3:
            rectangle1 = Rectangle(1, 2, 3, "sup'")
        self.assertEqual(str(err3.exception), "y must be an integer")

    def test_rectangle_value_error(self):
        with self.assertRaises(ValueError) as err:
            rectangle = Rectangle(-2, 1)
        self.assertEqual(str(err.exception), "width must be > 0")
        with self.assertRaises(ValueError) as err2:
            rectangle = Rectangle(2, 0)
        self.assertEqual(str(err2.exception), "height must be > 0")
        with self.assertRaises(ValueError) as err3:
            rectangle = Rectangle(0, 1)
        self.assertEqual(str(err3.exception), "width must be > 0")

    def test_rectangle_area(self):
        rectangle = Rectangle(3, 2)
        self.assertEqual(rectangle.area(), 6)

    def setUp(self):
        """Redirect stdout to capture print"""
        self.held, sys.stdout = sys.stdout, StringIO()
        """assign filename"""
        self.filename = "Rectangle.json"

    def tearDown(self):
        """Restore original stdout after test"""
        sys.stdout = self.held
        """Remove the file after the test to clean up."""
        if os.path.exists(self.filename):
            os.remove(self.filename)

    def test_rectangle_display_without_x_and_y(self):
        rectangle = Rectangle(3, 2, 0, 0)
        rectangle.display()
        self.assertEqual(sys.stdout.getvalue(), "###\n###\n")

    def test_display_without_y(self):
        rect = Rectangle(3, 2, 2, 0)
        rect.display()
        self.assertEqual(sys.stdout.getvalue(), "  ###\n  ###\n")

    def test_display(self):
        rect = Rectangle(2, 4, 1, 2)
        rect.display()
        self.assertEqual(sys.stdout.getvalue(), "\n\n ##\n ##\n ##\n ##\n")

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

    def test_rectangle_create_only_id(self):
        rectangle = Rectangle.create(**{ 'id': 89})
        self.assertEqual(rectangle.id, 89)
        self.assertEqual(rectangle.x, 0)

    def test_rectangle_create_id_width(self):
        rectangle = Rectangle.create(**{ 'id': 89, 'width': 1})
        self.assertEqual(rectangle.id, 89)
        self.assertEqual(rectangle.width, 1)

    def test_rectangle_create_id_width_height(self):
        rectangle = Rectangle.create(**{ 'id': 89, 'width': 1, 'height': 2})
        self.assertEqual(rectangle.id, 89)
        self.assertEqual(rectangle.width, 1)
        self.assertEqual(rectangle.height, 2)

    def test_rectangle_create_id_width_height_x(self):
        rectangle = Rectangle.create(**{ 'id': 89, 'width': 1, 'height': 2, 'x': 3})
        self.assertEqual(rectangle.id, 89)
        self.assertEqual(rectangle.width, 1)
        self.assertEqual(rectangle.height, 2)
        self.assertEqual(rectangle.x, 3)

    def test_rectangle_create_id_width_height_x_y(self):
        rectangle = Rectangle.create(**{ 'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4})
        self.assertEqual(rectangle.id, 89)
        self.assertEqual(rectangle.width, 1)
        self.assertEqual(rectangle.height, 2)
        self.assertEqual(rectangle.x, 3)
        self.assertEqual(rectangle.y, 4)

    def test_rectangle_save_to_file_none(self):
        Rectangle.save_to_file(None)
        self.assertTrue(os.path.exists(self.filename))
        with open(self.filename, 'r') as file:
            file_read = file.read()
            self.assertEqual(file_read, "[]")

    def test_rectangle_save_to_file_empty(self):
        Rectangle.save_to_file([])
        self.assertTrue(os.path.exists(self.filename))
        with open(self.filename, 'r') as file:
            file_read = file.read()
            self.assertEqual(file_read, "[]")

    def test_rectangle_save_to_file(self):
        rectangle = Rectangle(1, 2)
        Rectangle.save_to_file([rectangle])
        self.assertTrue(os.path.exists(self.filename))
        with open(self.filename, 'r') as file:
            file_read = file.read()
            expected_content = json.dumps([rectangle.to_dictionary()])
            self.assertEqual(json.loads(file_read), json.loads(expected_content))

    @classmethod
    def setUpClass(cls):
        cls.filename = "Rectangle.json"

    @classmethod
    def tearDownClass(cls):
        """Remove the file if it exists after tests."""
        if os.path.exists(cls.filename):
            os.remove(cls.filename)

    def test_rectangle_load_from_file_nofile(self):
        if os.path.exists(self.filename):
            os.remove(self.filename)
        result = Rectangle.load_from_file()
        self.assertEqual(result, [])

    def test_rectangle_load_from_file(self):
        rectangles = [
            {"id": 1, "width": 10, "height": 7, "x": 2, "y": 3},
            {"id": 2, "width": 3, "height": 4, "x": 0, "y": 0}
        ]
        with open(self.filename, "w") as file:
            file.write(Rectangle.to_json_string(rectangles))
        loaded_file = Rectangle.load_from_file()
        self.assertTrue(len(loaded_file) == len(rectangles))
        for loaded_rectangle, expected_rectangle in zip(loaded_file, rectangles):
            self.assertTrue(isinstance(loaded_rectangle, Rectangle))
            for key in expected_rectangle:
                self.assertEqual(getattr(loaded_rectangle,key), expected_rectangle[key])