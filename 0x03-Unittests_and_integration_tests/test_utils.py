import unittest
from unittest.mock import patch, Mock
from typing import Dict, List, Any

# Import the functions to be tested
from utils import access_nested_map, get_json, memoize

class TestAccessNestedMap(unittest.TestCase):
    def test_access_nested_map_valid_path(self):
        nested_map = {"a": {"b": {"c": 1}}}
        path = ["a", "b", "c"]
        self.assertEqual(access_nested_map(nested_map, path), 1)

    def test_access_nested_map_invalid_path(self):
        nested_map = {"a": 1}
        path = ["a", "b"]
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)
        self.assertEqual(str(context.exception), "'b'")

class TestGetJson(unittest.TestCase):
    @patch('utils.requests.get')
    def test_get_json(self, mock_get):
        test_url = "http://example.com"
        test_payload = {"key": "value"}
        
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_get.return_value = mock_response
        
        result = get_json(test_url)
        
        mock_get.assert_called_once_with(test_url)
        self.assertEqual(result, test_payload)

class TestMemoize(unittest.TestCase):
    def test_memoize(self):
        class TestClass:
            def __init__(self):
                self.call_count = 0
            
            @memoize
            def a_method(self):
                self.call_count += 1
                return 42
        
        obj = TestClass()
        
        first_call = obj.a_method
        second_call = obj.a_method
        
        self.assertEqual(first_call, 42)
        self.assertEqual(second_call, 42)
        self.assertEqual(obj.call_count, 1)

if __name__ == '__main__':
    unittest.main()
