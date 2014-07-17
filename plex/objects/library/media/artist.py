from plex.objects.base import Property
from plex.objects.directory import Directory
from plex.objects.library.media.container import MediaContainer
from plex.objects.library.metadata import Metadata


class Artist(Directory, Metadata):
    index = Property(type=int)

    def children(self):
        response = self.request('children')

        return self.parse(response, {
            'MediaContainer': (AlbumContainer, {
                'Directory': {
                    'album':    'Album',
                    None:       'Album'  # (All tracks)
                }
            })
        })


class AlbumContainer(MediaContainer, Artist):
    attribute_map = {
        'index':    'parentIndex',
        'title':    'parentTitle',
        '*':        '*'
    }
