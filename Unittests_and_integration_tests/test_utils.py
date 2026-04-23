#!/usr/bin/env python3
"""A module for unit tests"""

import unittest
from utils import access_nested_map
from parameterized import parameterized 

class TestAccessNestedMap(unittest.TestCase):

	@parameterized.expand([
		({"a": 1}, ("a",), 1),
		({"a": {"b": 2}}, ("a",), {"b": 2}),
		({"a": {"b": 2}}, ("a", "b"), 2)
		])

	def test_access_nested_map(self, nested_map, path, expected):
		"""Testing multiple elements"""
		self.assertEqual(access_nested_map(nested_map, path), expected)
		return nested_map, path, expected
