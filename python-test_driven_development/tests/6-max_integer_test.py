#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

	def test_max_at_end(self):
		max_at_end = [1, 2, 3, 4]
		self.assertAlmostEqual(max_integer(max_at_end), 4)

	def test_max_at_beginning(self):
		max_at_beginning = [4, 3, 2, 1]
		self.assertAlmostEqual(max_integer(max_at_beginning), 4)

	def test_max_in_middle(self):
		malcolm_in_the_middle = [1, 4, 5, 2, 3]
		self.assertAlmostEqual(max_integer(malcolm_in_the_middle), 5)

	def test_one_negative(self):
		one_negative = [1, 2, -3, 4]
		self.assertAlmostEqual(max_integer(one_negative), 4)

	def test_all_negative(self):
		all_negative = [-1, -2, -3, -4]
		self.assertAlmostEqual(max_integer(all_negative), -1)

	def test_one_in_list(self):
		one_in_list = [4]
		self.assertAlmostEqual(max_integer(one_in_list), 4)

	def test_list_empty(self):
		empty = []
		self.assertAlmostEqual(max_integer(empty), None)