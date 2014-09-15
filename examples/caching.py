import logging
from shove import Shove

logging.basicConfig(level=logging.DEBUG)

from plex import Plex
import os


def print_title(container):
    print list(container)[0].title


if __name__ == '__main__':
    # Without caching
    print_title(Plex['library'].metadata(3))
    print_title(Plex['library'].metadata(3))

    print

    # Build shove
    cache_dir = os.path.abspath('cache')
    print 'cache_dir: %r' % cache_dir

    cache = Shove('file://%s' % cache_dir, 'memory://', optimize=False)

    # With caching
    print_title(Plex['library'].use(cache).metadata(3))
    print_title(Plex['library'].use(cache).metadata(3))

    # close cache (sync back to disk)
    cache.close()
