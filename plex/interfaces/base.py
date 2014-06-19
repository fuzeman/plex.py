from functools import wraps
from lxml import etree
import logging

log = logging.getLogger(__name__)


class Interface(object):
    path = None

    def __init__(self, client):
        self.client = client

    def __getitem__(self, name):
        if hasattr(self, name):
            return getattr(self, name)

        raise ValueError('Unknown action "%s" on %s', name, self)

    def request(self, path, params=None, data=None, **kwargs):
        return self.client.request(
            '%s/%s' % (self.path, path),
            params, data,
            **kwargs
        )

    def parse(self, response, schema):
        root = etree.fromstring(response.content)

        return self.construct(root, schema)

    def construct(self, node, schema):
        if not schema:
            raise ValueError('Missing schema for node with tag "%s"' % node.tag)

        item = schema.get(node.tag)

        if item is None:
            raise ValueError('Unknown node with tag "%s"' % node.tag)

        if type(item) is dict:
            item = item.get(node.get('type'))

            if item is None:
                raise ValueError('Unknown node type "%s"' % node.get('type'))

        descriptor = None
        child_schema = None

        if type(item) is tuple and len(item) == 2:
            descriptor, child_schema = item
        else:
            descriptor = item

        #print 'node: %s, descriptor: %s, child_schema: %s' % (node, descriptor, child_schema)

        obj = descriptor.construct(node)

        # Lazy-construct children
        def iter_children():
            for child_node in node:
                yield self.construct(child_node, child_schema)

        obj._children = iter_children()

        return obj


class InterfaceProxy(object):
    def __init__(self, interface, args):
        self.interface = interface
        self.args = list(args)

    def __getattr__(self, name):
        value = getattr(self.interface, name)

        if not hasattr(value, '__call__'):
            return value

        @wraps(value)
        def wrap(*args, **kwargs):
            args = self.args + list(args)

            return value(*args, **kwargs)

        return wrap
