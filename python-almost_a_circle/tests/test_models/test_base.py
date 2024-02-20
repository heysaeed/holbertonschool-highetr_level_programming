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
        self.assertEqual(json_string, [])
