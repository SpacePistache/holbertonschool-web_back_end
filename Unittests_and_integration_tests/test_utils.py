#!/usr/bin/env python3
"""A module for unit tests"""

import unittest
from utils import access_nested_map
from utils import get_json
from parameterized import parameterized
from unittest.mock import patch, Mock


class TestAccessNestedMap(unittest.TestCase):

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Test normal cases"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """Test that KeyError is raised"""
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)

        self.assertEqual(context.exception.args[0], path[-1])


class TestGetJson(unittest.TestCase):
    """Use Mocking to test HTTP calls"""

    @patch("utils.requests.get")
    def test_get_json(self, mock_get):

        mock_http_call = Mock()
        mock_http_call.json.return_value = {"key": "value"}
        mock_get.return_value = mock_http_call

        result = get_json("http://example.com")

        self.assertEqual(result, {"key": "value"})
