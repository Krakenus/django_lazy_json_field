from unittest import TestCase

from lazy_json_field.utils import LazyJSONDict


class LazyJsonTestCase(TestCase):
    def setUp(self):
        self.raw_json = '{"key": "value"}'

    def test_lazy_json(self):
        lazy_json = LazyJSONDict(self.raw_json)

        self.assertEqual(str(lazy_json), self.raw_json)
        self.assertFalse(bool(lazy_json.data))
        self.assertEqual(lazy_json['key'], 'value')
        self.assertTrue(bool(lazy_json.data))
