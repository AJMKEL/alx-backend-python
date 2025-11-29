#!/usr/bin/env python3
"""
Unit tests for utils module.

This module contains test cases for the utility functions defined in utils.py,
specifically testing the access_nested_map function with various inputs.
"""

import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """
    Test case class for the access_nested_map function.
    
    This class tests the access_nested_map function to ensure it correctly
    retrieves values from nested dictionaries using a path sequence.
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """
        Test that access_nested_map returns the expected result.
        
        Args:
            nested_map: A nested dictionary to navigate
            path: A tuple representing the path to the desired value
            expected: The expected return value
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)


if __name__ == "__main__":
    unittest.main()
