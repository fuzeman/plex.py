from plex.objects.base import Property
from plex.objects.library.video import Video


class Movie(Video):
    rating_key = Property('ratingKey')

    original_title = Property('originalTitle')

    summary = Property
    studio = Property
    year = Property(type=int)
    content_rating = Property('contentRating')

    rating = Property('rating', type=float)

    view_offset = Property('viewOffset', type=int)
    duration = Property('duration', type=int)

    added_at = Property('addedAt')
    last_viewed_at = Property('lastViewedAt')
    originally_available_at = Property('originallyAvailableAt')
