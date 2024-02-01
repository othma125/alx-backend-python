#!/usr/bin/env python3
""" test utils """
from unittest import TestCase, mock
from utils import access_nested_map, get_json, memoize
from unittest import mock


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


class TestGetJson(TestCase):
    """ test get json """
    def test_get_json(self):
        """ test get json """
        test_url = "http://example.com"
        test_payload = {"payload": True}

        with mock.patch('requests.get') as mock_get:
            mock_response = mock.Mock()
            mock_response.json.return_value = test_payload
            mock_get.return_value = mock_response

            result = get_json(test_url)

            mock_get.assert_called_once_with(test_url)
            self.assertEqual(result, test_payload)

        test_url = "http://holberton.io"
        test_payload = {"payload": False}

        with mock.patch('requests.get') as mock_get:
            mock_response = mock.Mock()
            mock_response.json.return_value = test_payload
            mock_get.return_value = mock_response

            result = get_json(test_url)

            mock_get.assert_called_once_with(test_url)
            self.assertEqual(result, test_payload)


class TestMemoize(TestCase):
    """ test memoize """
    def test_memoize(self):
        """ test memoize """
        class TestClass:
            """ test class """
            def a_method(self):
                """ test method """
                return 42

            @memoize
            def a_property(self):
                """ test property """
                return self.a_method()

        with mock.patch.object(TestClass, 'a_method',
                               return_value=42) as mock_method:
            test = TestClass()
            test.a_property
            test.a_property

            mock_method.assert_called_once()
