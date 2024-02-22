import json
import collections


class LazyJSONEncoder(json.JSONEncoder):

    def encode(self, o):
        if isinstance(o, (LazyJSONDict, LazyJSONList)):
            return str(o)
        return super().encode(o)


class LazyJSONMixin:

    def __init__(self, data, /, decoder=None, **kwargs):
        self.__str_data = data
        self.__decoder = decoder
        self._parsed_data = None

    @property
    def data(self):
        if not self._parsed_data:
            try:
                self._parsed_data = json.loads(self.__str_data, cls=self.__decoder)
            except json.JSONDecodeError:
                pass
        return self._parsed_data

    def __str__(self):
        return self.__str_data


class LazyJSONDict(LazyJSONMixin, collections.UserDict):
    pass


class LazyJSONList(LazyJSONMixin, collections.UserList):
    pass
