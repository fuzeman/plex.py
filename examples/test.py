from plex import Plex
import logging

logging.basicConfig(level=logging.DEBUG)


if __name__ == '__main__':
    sections = Plex['library'].sections()
    print sections, '-', sections.__dict__

    for section in sections:
        print '\t', section, '-', section.__dict__
