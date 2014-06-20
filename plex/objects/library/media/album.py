from plex.objects.base import Property
from plex.objects.directory import Directory
from plex.objects.library.metadata import Metadata
from plex.objects.library.media.artist import Artist


class Album(Directory, Metadata):
    artist = Property(resolver=lambda: Album.construct_artist)

    index = Property

    year = Property(type=int)
    originally_available_at = Property('originallyAvailableAt')

    track_count = Property('leafCount', int)
    viewed_track_count = Property('viewedLeafCount', int)

    @staticmethod
    def construct_artist(node):
        attribute_map = {
            'key': 'parentKey',
            'ratingKey': 'parentRatingKey',
            'thumb': 'parentThumb',
            'title': 'parentTitle'
        }

        return attribute_map.values(), Artist.construct(node, attribute_map)