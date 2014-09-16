class ConfigurationManager(object):
    def __init__(self):
        self.stack = [
            Configuration(self)
        ]

    @property
    def current(self):
        return self.stack[-1]

    def cache(self, **definitions):
        return Configuration(self).cache(**definitions)

    def server(self, host='127.0.0.1', port=32400):
        return Configuration(self).server(host, port)

    def get(self, key, default=None):
        return self.current.get(key, default)

    def __getitem__(self, key):
        return self.current[key]


class Configuration(object):
    def __init__(self, manager):
        self.manager = manager

        self.data = {}

    def cache(self, **definitions):
        self.data['cache'] = definitions

        return self

    def server(self, host='127.0.0.1', port=32400):
        self.data['server'] = {
            'host': host,
            'port': port
        }

        return self

    def get(self, key, default=None):
        return self.data.get(key, default)

    def __enter__(self):
        self.manager.stack.append(self)

    def __exit__(self, exc_type, exc_val, exc_tb):
        item = self.manager.stack.pop()

        assert item == self

    def __getitem__(self, key):
        return self[key]
