#!/usr/bin/env python3
""" test utils """
from unittest import TestCase
from utils import access_nested_map


class TestAccessNestedMap(TestCase):
    """ test access nested map """
    def test_access_nested_map(self):
        """ test access nested map """
        nested_map = {'a': 1}
        self.assertEqual(access_nested_map(nested_map, path=('a')), 1)
        nested_map = {'a': {'b': 2}}
        self.assertEqual(access_nested_map(nested_map, path=('a')), {"b": 2})
        self.assertEqual(access_nested_map(nested_map, path=('a', 'b')), 2)

    def test_access_nested_map_exception(self):
        """ test access nested map exception """
        nested_map = {}
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path=('a'))

        nested_map = {'a': 1}
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path=('a', 'b'))
