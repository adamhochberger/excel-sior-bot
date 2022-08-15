import enum


class BaseEnum(enum.Enum):
    @classmethod
    def values_list(cls):
        return list(map(lambda c: c.value, cls))