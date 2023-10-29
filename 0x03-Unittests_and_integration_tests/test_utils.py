#!/usr/bin/env python3

"""unittest"""
import unittest
from parameterized import parameterized
from utils import access_nested_map

class TestAccessNestedMap(unittest.TestCase):
    """Unit tests for the access_nested_map function."""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        """
        Test the access_nested_map function.

        Parameters:
        - nested_map (Mapping): A nested map.
        - path (Sequence): A sequence of keys representing a path to the value.
        - expected_result (Any): The expected result.

        Returns:
        - None

        Raises:
        - AssertionError: If the actual result does not match the expected result.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected_result)

if __name__ == '__main__':
    unittest.main()
