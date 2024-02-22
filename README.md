# Django Lazy JSON Field

Wrapper for Django's JSONField that allows for lazy loading of the JSON object.

## Why?

Django's JSONField is great, but it's not lazy. This means that if you have a large JSON object,
it will be loaded into memory every time you access the field.
This can be a problem if you have a large number of records with large JSON objects.

This package provides a `LazyJSONField` that only loads the JSON object when it's accessed.

## Installation

```bash
pip install django-lazy-json-field
```

## Usage

```python
from django.db import models
from lazy_json_field.fields import LazyJSONField

class MyModel(models.Model):
    data = LazyJSONField()
```
