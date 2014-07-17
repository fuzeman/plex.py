from plex.interfaces.core.base import Interface


class SectionInterface(Interface):
    path = 'library/sections'

    def all(self, key):
        response = self.request(key, 'all')

        return self.parse(response, {
            'MediaContainer': ('MediaContainer', {
                'Directory': {
                    'artist':   'Artist',
                    'show':     'Show'
                },
                'Video': {
                    'movie':    'Movie'
                }
            })
        })
