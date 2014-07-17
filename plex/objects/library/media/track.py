from plex.objects.base import Property
from plex.objects.directory import Directory
from plex.objects.library.media.album import Album
from plex.objects.library.metadata import Metadata


class Track(Directory, Metadata):
    album = Property(resolver=lambda: Track.construct_album)

    index = Property(type=int)

    duration = Property(type=int)

    @staticmethod
    def construct_album(client, node):
        attribute_map = {
            'key':          'parentKey',
            'ratingKey':    'parentRatingKey'
        }

        return Album.construct(client, node, attribute_map, child=True)
