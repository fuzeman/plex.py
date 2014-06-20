import logging

log = logging.getLogger(__name__)


class Property(object):
    def __init__(self, name=None, type=None, resolver=None):
        self.name = name
        self.type = type
        self.resolver = resolver

    def value(self, key, node, keys_used):
        if self.resolver is not None:
            return self.value_func(node, keys_used)

        return self.value_node(key, node, keys_used)

    def value_node(self, key, node, keys_used):
        value = node.get(key)
        keys_used.append(key)

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

    def value_func(self, node, keys_used):
        try:
            func = self.resolver()
            keys, value = func(node)

            keys_used.extend(keys)
            return value
        except Exception, ex:
            log.warn(ex)
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
                yield key, value


    @classmethod
    def construct(cls, node, attribute_map=None):
        keys_available = attribute_map.keys() if attribute_map else node.keys()
        keys_used = []

        obj = cls()

        for key, prop in obj.properties():
            node_key = prop.name or key

            if attribute_map:
                if node_key not in attribute_map:
                    setattr(obj, key, None)
                    continue

                node_key = attribute_map.get(key)

            if key == 'title':
                pass

            setattr(obj, key, prop.value(node_key, node, keys_used))

        omitted = list(set(keys_available) - set(keys_used))
        omitted.sort()

        if omitted:
            log.warn('%s construction omitted attributes: %s', cls.__name__, ', '.join(omitted))

        return obj

    def __iter__(self):
        return self._children or []
