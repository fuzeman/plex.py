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

    print '-' * 40

    # Show
    container = Plex['library'].metadata(1)

    show = list(container)[0]

    print '[Show] %s' % show.title

    for season in show.children():
        print '\t[Season] %s' % season.title


    exit(0)




    # Movie
    container = Plex['library'].metadata(12)
    item = list(container)[0]

    print item.title
