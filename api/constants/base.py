from collections import namedtuple
from enum import Enum


class BaseEnum(Enum):
    def __repr__(self):
        return self.value

    def __str__(self):
        return self.value

    @classmethod
    def get_all_values(cls):
        return list(map(lambda c: c.value, cls))

    @classmethod
    def get_all_keys(cls):
        return list(map(lambda c: c.name, cls))

    @classmethod
    def get_all_named_tuple(cls):
        EnumTuple = namedtuple('enum_tuple', ['name', 'value'])
        return list(map(lambda c: EnumTuple(c.name, c.value), cls))
