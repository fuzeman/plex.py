from plex.objects.base import Property
from plex.objects.directory import Directory


class Video(Directory):
    rating = Property(type=float)
    user_rating = Property('userRating', type=float)

    view_count = Property('viewCount', type=int)
    view_offset = Property('viewOffset', type=int)
