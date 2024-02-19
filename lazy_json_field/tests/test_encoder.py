from unittest import TestCase

from lazy_json_field.lazy_json import LazyJSONDict, LazyJSONEncoder


class LazyJSONEncoderTestCase(TestCase):

    def test_lazy_json_object(self):
        lazy_json = LazyJSONDict('{"key": "value"}')
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
