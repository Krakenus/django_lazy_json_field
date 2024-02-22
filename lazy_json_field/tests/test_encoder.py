import json
from unittest import TestCase

from lazy_json_field.lazy_json import LazyJSONDict, LazyJSONEncoder, LazyJSONList


class LazyJSONEncoderTestCase(TestCase):

    def test_lazy_json_dict(self):
        lazy_json = LazyJSONDict('{"key": "value"}')
        encoder = LazyJSONEncoder()
        self.assertEqual(encoder.encode(lazy_json), str(lazy_json))

    def test_lazy_json_list(self):
        lazy_json = LazyJSONList('["value"]')
        encoder = LazyJSONEncoder()
        self.assertEqual(encoder.encode(lazy_json), str(lazy_json))

    def test_regular_dict(self):
        regular_dict = {"key": "value"}
        encoder = LazyJSONEncoder()
        self.assertEqual(encoder.encode(regular_dict), '{"key": "value"}')

    def test_regular_string(self):
        regular_string = '{"key": "value"}'
        encoder = LazyJSONEncoder()
        self.assertEqual(encoder.encode(regular_string), '"{\\"key\\": \\"value\\"}"')

    def test_regular_list(self):
        regular_list = ["value"]
        encoder = LazyJSONEncoder()
        self.assertEqual(encoder.encode(regular_list), '["value"]')


class LazyJSONSerializationTestCase(TestCase):

    def test_lazy_json_dict(self):
        with self.assertRaises(TypeError):
            json.dumps(LazyJSONDict('{"key": "value"}'))
        self.assertEqual(
            json.dumps(
                LazyJSONDict('{"key": "value"}'),
                cls=LazyJSONEncoder
            ),
            '{"key": "value"}'
        )

    def test_lazy_json_list(self):
        with self.assertRaises(TypeError):
            json.dumps(LazyJSONList('["value"]'))
        self.assertEqual(
            json.dumps(
                LazyJSONList('["value"]'),
                cls=LazyJSONEncoder
            ),
            '["value"]'
        )
