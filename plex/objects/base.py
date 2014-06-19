class Property(object):
    def __init__(self, name=None, type=None):
        self.name = name
        self.type = type


class Descriptor(object):
    def __init__(self):
        self._children = None

    @classmethod
    def properties(cls):
        for key in dir(cls):
            if key.startswith('_'):
                continue

            value = getattr(self, key)

            if value is Property:
                yield Property(key)
            elif isinstance(value, Property):
                if value.name is None:
                    value.name = key

                yield value


    @classmethod
    def construct(cls, node):
        return cls()

    def __iter__(self):
        return self._children or []
