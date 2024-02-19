import json
from collections import UserDict


class LazyJSONEncoder(json.JSONEncoder):

    def encode(self, o):
        if isinstance(o, LazyJSONDict):
            return str(o)
        return super().encode(o)


class LazyJSONDict(UserDict):

    def __init__(self, data, /, decoder=None, **kwargs):
        self.__str_data = data
        self.__decoder = decoder
        super().__init__(**kwargs)

    def _parse_data(self):
        if not self.data:
            try:
                self.data = json.loads(self.__str_data, cls=self.__decoder)
            except json.JSONDecodeError:
                pass

    def __len__(self):
        self._parse_data()
        return super().__len__()

    def __getitem__(self, item):
        self._parse_data()
        return super().__getitem__(item)

    def __setitem__(self, key, value):
        self._parse_data()
        super().__setitem__(key, value)

    def __delitem__(self, key):
        self._parse_data()
        super().__delitem__(key)

    def __iter__(self):
        self._parse_data()
        return super().__iter__()

    def __contains__(self, item):
        self._parse_data()
        return super().__contains__(item)

    def __repr__(self):
        self._parse_data()
        return super().__repr__()

    def __str__(self):
        return self.__str_data

    def __or__(self, other):
        self._parse_data()
        return super().__or__(other)

    def __ror__(self, other):
        self._parse_data()
        return super().__ror__(other)

    def __ior__(self, other):
        self._parse_data()
        return super().__ior__(other)

    def __copy__(self):
        self._parse_data()
        return super().__copy__()
