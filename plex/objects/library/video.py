from plex.objects.base import Property
from plex.objects.directory import Directory


class Video(Directory):
    view_count = Property('viewCount', type=int)
    view_offset = Property('viewOffset', type=int)

    duration = Property(type=int)
