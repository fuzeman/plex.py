from plex import Plex
from plex.objects.library.metadata.album import Album
from plex.objects.library.metadata.movie import Movie
from plex.objects.library.metadata.season import Season

import logging

logging.basicConfig(level=logging.DEBUG)


def recently_added():
    container = Plex['library'].recently_added()

    for item in container:
        if type(item) is Album:
            print '[Album]', item.title
            print '\t[Artist]', item.artist.title
        elif type(item) is Movie:
            print '[Movie]', item.title
        elif type(item) is Season:
            print '[Season][S%02d] %s' % (item.index, item.title)
        else:
            print item


def metadata_show():
    container = Plex['library'].metadata(1)
    show = list(container)[0]

    print '[Show] %s (rating_key: %s)' % (show.title, show.rating_key)

    for episode in show.all_leaves():
        print '\t\t[Episode][S%02dE%02d] %s (rating_key: %s)' % (episode.season.index, episode.index, episode.title, episode.rating_key)

    for season in show.children():
        print '\t[Season][S%02d] %s (rating_key: %s)' % (season.index, season.title, season.rating_key)

        for episode in season.children():
            print '\t\t[Episode][S%02dE%02d] %s (rating_key: %s)' % (season.index, episode.index, episode.title, episode.rating_key)


def metadata_movie():
    container = Plex['library'].metadata(12)
    movie = list(container)[0]

    print '[Movie] %s (rating_key: %s)' % (movie.title, movie.rating_key)


if __name__ == '__main__':
    recently_added()
    print '-' * 50
    metadata_show()
    print '-' * 50
    metadata_movie()
