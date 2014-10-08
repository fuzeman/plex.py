import pytest
import sys
import types


def test_import():
    # Try import extension that doesn't exist
    with pytest.raises(ImportError):
        __import__('plex.ext.missing')

    # Create dummy extension module
    sys.modules['plex_dummy'] = types.ModuleType('plex_dummy', 'Dummy plex extension for tests')
    sys.modules['plex_dummy'].__dict__.update({'TEST': 1})

    # Try import dummy extension
    from plex.ext import dummy

    assert dummy.TEST == 1
