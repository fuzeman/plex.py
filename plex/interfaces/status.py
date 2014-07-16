from plex.interfaces.base import Interface


class StatusInterface(Interface):
    path = 'status'

    def sessions(self):
        response = self.request('sessions')

        return self.parse(response, {
            'MediaContainer': ('MediaContainer', {
                'Video': {
                    'episode':  'Episode',
                    'movie':    'Movie'
                }
            })
        })
