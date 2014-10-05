import os

TESTS_PATH = os.path.abspath(os.path.dirname(__file__).replace('\\core', ''))


def read(path):
    if not os.path.isabs(path):
        path = os.path.join(TESTS_PATH, path)

    path = os.path.abspath(path)

    with open(path, 'r') as fp:
        return fp.read()
