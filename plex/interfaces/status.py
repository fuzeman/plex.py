from plex.core.idict import idict
from plex.interfaces.core.base import Interface


class StatusInterface(Interface):
    path = 'status'

    def sessions(self):
        response = self.http.get('sessions')

        return self.parse(response, idict({
            'MediaContainer': ('SessionContainer', idict({
                'Photo': {
                    'photo':    'Photo'
                },
                'Video': {
                    'episode':  'Episode',
                    'clip':     'Clip',
                    'movie':    'Movie'
                },

                'Track': 'Track'
            }))
        }))
