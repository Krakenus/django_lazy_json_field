from unittest import TestCase

from lazy_json_field.lazy_json import LazyJSONDict, LazyJSONList


class LazyJsonDictTestCase(TestCase):
    def setUp(self):
        self.raw_json = '{"key": "value"}'

    def test_lazy_json(self):
        lazy_json = LazyJSONDict(self.raw_json)

        self.assertEqual(str(lazy_json), self.raw_json)
        self.assertIsNone(lazy_json._parsed_data)
        self.assertEqual(lazy_json['key'], 'value')
        self.assertIsNotNone(lazy_json._parsed_data)

    def test_lazy_parse_called(self):
        lazy_json = LazyJSONDict(self.raw_json)
        self.assertEqual(str(lazy_json), self.raw_json)
        self.assertIsNone(lazy_json._parsed_data)
        lazy_json.data['key']
        self.assertIsNotNone(lazy_json._parsed_data)


class LazyJsonListTestCase(TestCase):
    def setUp(self):
        self.raw_json = '["value"]'

    def test_lazy_json(self):
        lazy_json = LazyJSONList(self.raw_json)

        self.assertEqual(str(lazy_json), self.raw_json)
        self.assertIsNone(lazy_json._parsed_data)
        self.assertEqual(lazy_json[0], 'value')
        self.assertTrue(bool(lazy_json._parsed_data))

    def test_lazy_parse_called(self):
        lazy_json = LazyJSONList(self.raw_json)
        self.assertEqual(str(lazy_json), self.raw_json)
        self.assertIsNone(lazy_json._parsed_data)
        lazy_json[0]
        self.assertIsNotNone(lazy_json._parsed_data)
