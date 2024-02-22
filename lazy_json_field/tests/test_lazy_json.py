import json
from unittest import TestCase
from unittest.mock import patch

from lazy_json_field.lazy_json import LazyJSONDict, LazyJSONList


class LazyJsonDictTestCase(TestCase):
    def setUp(self):
        self.raw_json = '{"key": "value"}'

    def test_lazy_json(self):
        lazy_json = LazyJSONDict(self.raw_json)

        self.assertEqual(str(lazy_json), self.raw_json)
        self.assertFalse(bool(lazy_json._parsed_data))
        self.assertEqual(lazy_json['key'], 'value')
        self.assertTrue(bool(lazy_json._parsed_data))

    def test_lazy_parse_called(self):
        lazy_json = LazyJSONDict(self.raw_json)
        with patch('lazy_json_field.lazy_json.LazyJSONMixin.data') as data_mock:
            self.assertEqual(str(lazy_json), self.raw_json)
            self.assertFalse(data_mock.called)
            lazy_json.data['key']
            self.assertTrue(data_mock.assert_called_once)


class LazyJsonListTestCase(TestCase):
    def setUp(self):
        self.raw_json = '["value"]'

    def test_lazy_json(self):
        lazy_json = LazyJSONList(self.raw_json)

        self.assertEqual(str(lazy_json), self.raw_json)
        self.assertFalse(bool(lazy_json._parsed_data))
        self.assertEqual(lazy_json[0], 'value')
        self.assertTrue(bool(lazy_json._parsed_data))

    def test_lazy_parse_called(self):
        lazy_json = LazyJSONList(self.raw_json)
        with patch('lazy_json_field.lazy_json.LazyJSONMixin.data') as data_mock:
            self.assertEqual(str(lazy_json), self.raw_json)
            self.assertFalse(data_mock.called)
            lazy_json[0]
            self.assertTrue(data_mock.assert_called_once)
