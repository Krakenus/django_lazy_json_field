from django.db.models.fields.json import JSONField, KeyTransform

from lazy_json_field.lazy_json import LazyJSONDict, LazyJSONEncoder


class LazyJSONField(JSONField):

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('encoder', LazyJSONEncoder)
        super().__init__(*args, **kwargs)

    def from_db_value(self, value, expression, connection):
        if value is None:
            return value
        # Some backends (SQLite at least) extract non-string values in their
        # SQL datatypes.
        if isinstance(expression, KeyTransform) and not isinstance(value, str):
            return value
        # the only difference from parent class
        return LazyJSONDict(value, decoder=self.decoder)

    def value_to_string(self, obj):
        return str(self.value_from_object(obj))
