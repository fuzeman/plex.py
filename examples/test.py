from plex import Plex
from plex.objects.library.media.album import Album
from plex.objects.library.media.movie import Movie
from plex.objects.library.media.season import Season

import logging

logging.basicConfig(level=logging.DEBUG)


if __name__ == '__main__':
    container = Plex['library'].recently_added()

    for item in container:
        if type(item) is Album:
            print '[Album]', item.title
            print '\t[Artist]', item.artist.title
        elif type(item) is Movie:
            print '[Movie]', item.title
        elif type(item) is Season:
            print '[Season]', item.title
        else:
            print item
