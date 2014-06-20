from plex.objects.base import Property
from plex.objects.library.metadata import Metadata
from plex.objects.library.video import Video


class Movie(Video, Metadata):
    studio = Property
    content_rating = Property('contentRating')

    year = Property(type=int)
    originally_available_at = Property('originallyAvailableAt')

    tagline = Property
