from plex.interfaces.base import Interface
from plex.objects.library.container import Container
from plex.objects.library.location import Location
from plex.objects.library.media.album import Album
from plex.objects.library.media.movie import Movie
from plex.objects.library.media.season import Season
from plex.objects.library.media.show import Show
from plex.objects.library.section import Section


class LibraryInterface(Interface):
    path = 'library'

    def metadata(self, rating_key):
        response = self.request('metadata', rating_key)

        return self.parse(response, {
            'MediaContainer': (Container, {
                'Directory': {
                    'album': Album,
                    'season': Season,
                    'show': Show
                },
                'Video': {
                    'movie': Movie
                }
            })
        })

    def on_deck(self):
        raise NotImplementedError()

    def recently_added(self):
        response = self.request('recentlyAdded')

        return self.parse(response, {
            'MediaContainer': (Container, {
                'Directory': {
                    'album': Album,
                    'season': Season
                },
                'Video': {
                    'movie': Movie
                }
            })
        })

    def sections(self):
        response = self.request('sections')

        return self.parse(response, {
            'MediaContainer': (Container, {
                'Directory': (Section, {
                    'Location': Location
                })
            })
        })
