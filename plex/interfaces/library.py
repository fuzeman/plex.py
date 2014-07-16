from plex.interfaces.base import Interface


class LibraryInterface(Interface):
    path = 'library'

    def metadata(self, rating_key):
        response = self.request('metadata', rating_key)

        return self.parse(response, {
            'MediaContainer': ('MediaContainer', {
                'Directory': {
                    'album':    'Album',
                    'season':   'Season',
                    'show':     'Show'
                },
                'Video': {
                    'movie':    'Movie'
                }
            })
        })

    def on_deck(self):
        raise NotImplementedError()

    def recently_added(self):
        response = self.request('recentlyAdded')

        return self.parse(response, {
            'MediaContainer': ('MediaContainer', {
                'Directory': {
                    'album':    'Album',
                    'season':   'Season'
                },
                'Video': {
                    'movie':    'Movie'
                }
            })
        })

    def sections(self):
        response = self.request('sections')

        return self.parse(response, {
            'MediaContainer': ('MediaContainer', {
                'Directory': ('Section', {
                    'Location': 'Location'
                })
            })
        })
