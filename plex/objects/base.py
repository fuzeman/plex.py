import logging

log = logging.getLogger(__name__)


class Property(object):
    def __init__(self, name=None, type=None):
        self.name = name
        self.type = type

    def value(self, node):
        value = node.get(self.name)

        if value is None:
            return None

        # Return string
        if not self.type:
            return value

        # Convert to specified type
        try:
            return self.type(value)
        except:
            return None


class Descriptor(object):
    def __init__(self):
        self._children = None

    def properties(self):
        for key in dir(self):
            if key.startswith('_'):
                continue

            value = getattr(self, key)

            if value is Property:
                yield key, Property(key)
            elif isinstance(value, Property):
                if value.name is None:
                    value.name = key

                yield key, value


    @classmethod
    def construct(cls, node):
        obj = cls()
        keys = []

        for key, prop in obj.properties():
            setattr(obj, key, prop.value(node))
            keys.append(prop.name)

        omitted = list(set(node.keys()) - set(keys))
        omitted.sort()

        if omitted:
            log.warn('%s construction omitted attributes: %s', cls.__name__, ', '.join(omitted))

        return obj

    def __iter__(self):
        return self._children or []
