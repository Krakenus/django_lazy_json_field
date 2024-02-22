from django.test import TestCase

from example_project.test_app.models import TestModel
from lazy_json_field.lazy_json import LazyJSONDict, LazyJSONList


class LazyJsonTestCase(TestCase):
    fixtures = ['test_model.json']

    def test_simple_objects_deferred_parsing(self):
        for obj in TestModel.objects.filter(name__startswith='simple'):
            str(obj.lazy_data)
            self.assertIsNone(obj.lazy_data._parsed_data)
            if isinstance(obj.lazy_data, LazyJSONDict):
                try:
                    self.assertTrue(obj.lazy_data['lazy'])
                except KeyError:
                    pass
            elif isinstance(obj.lazy_data, LazyJSONList):
                self.assertTrue(obj.lazy_data[1])
            self.assertIsNotNone(obj.lazy_data._parsed_data)

    def test_nested_dict_deferred_parsing(self):
        obj = TestModel.objects.get(name='nested dict')
        str(obj.lazy_data)
        self.assertIsNone(obj.lazy_data._parsed_data)
        self.assertTrue(isinstance(obj.lazy_data, LazyJSONDict))
        try:
            self.assertTrue(obj.lazy_data['data']['lazy'])
        except KeyError:
            pass
        self.assertIsNotNone(obj.lazy_data._parsed_data)
