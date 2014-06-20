from plex.objects.base import Property
from plex.objects.library.metadata import Metadata
from plex.objects.library.video import Video


class Movie(Video, Metadata):
    summary = Property
    studio = Property
    year = Property(type=int)
    content_rating = Property('contentRating')

    view_offset = Property('viewOffset', type=int)

    added_at = Property('addedAt')
    last_viewed_at = Property('lastViewedAt')
    originally_available_at = Property('originallyAvailableAt')
