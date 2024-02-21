#!/usr/bin/python3
import unittest
import json
from models.base import Base


class TestBase(unittest.TestCase):

    def test_assign_id(self):
        test = Base(50)
        self.assertEqual(test.id, 50)

    def test_no_id_assigned(self):
        test = Base()
        self.assertEqual(test.id, 1)

    def test_to_json_string(self):
        dictionary = {'id': 50,
                      'width': 10,
                      'height': 5,
                      'x': 2,
                      'y': 3}
        json_string = Base.to_json_string(dictionary)
        self.assertTrue(isinstance(json_string, str))

    def test_to_json_string_content(self):
        dictionary = {'id': 50,
                      'width': 10,
                      'height': 5,
                      'x': 2,
                      'y': 3}
        json_string = Base.to_json_string(dictionary)
        self.assertCountEqual(json.loads(json_string), dictionary)

    def test_to_json_string_none(self):
        json_string = Base.to_json_string(None)
        self.assertEqual(json_string, "[]")

    def test_from_json_string(self):
        string = '[{"id": 1, "width": 10, "height": 7, "x": 2, "y": 8}]'
        json_list = Base.from_json_string(string)
        self.assertTrue(isinstance(json_list, list))

    def test_from_json_string_content(self):
        string = '[{"id": 1, "width": 10, "height": 7, "x": 2, "y": 8}]'
        expected_list = [{'id': 1, 'width': 10, 'height': 7, 'x': 2, 'y': 8}]
        json_list = Base.from_json_string(string)
        self.assertEqual(json_list, expected_list)

    def test_from_json_string_none(self):
        json_list = Base.from_json_string(None)
        self.assertEqual(json_list, [])

    def test_create_error(self):
        with self.assertRaises(Exception) as err:
            Base.create()
        self.assertEqual(str(err.exception), "Wrong class") # change error msg to your own