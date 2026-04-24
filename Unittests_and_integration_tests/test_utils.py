#!/usr/bin/env python3
"""A module for unit tests"""

import unittest
from utils import access_nested_map
from utils import get_json
from parameterized import parameterized
from unittest.mock import patch, Mock
from utils import memoize


class TestAccessNestedMap(unittest.TestCase):
    """Class test for nested maps"""

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

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch("utils.requests.get")
    def test_get_json(self, url, payload, mock_get):
        """testing json"""

        mock_http_call = Mock()
        mock_http_call.json.return_value = payload
        mock_get.return_value = mock_http_call

        result = get_json(url)

        self.assertEqual(result, payload)
        mock_get.assert_called_once_with(url)


class TestMemoize(unittest.TestCase):
    """Test memoization decorator"""

    def test_memoize(self):
        """Test that memoize caches result"""

        class TestClass:
            def a_method(self):
                """test class"""
                return 42

            @memoize
            def a_property(self):
                """method function"""
                return self.a_method()

        with patch.object(TestClass, "a_method",
                          return_value=42) as mock_method:
            obj = TestClass()

            result1 = obj.a_property
            result2 = obj.a_property

            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)
            mock_method.assert_called_once()
