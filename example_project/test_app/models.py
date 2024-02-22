from django.db import models

from lazy_json_field.fields import LazyJSONField


class TestModel(models.Model):
    name = models.CharField(max_length=100)
    eager_data = models.JSONField()
    lazy_data = LazyJSONField()
