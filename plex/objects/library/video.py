from plex.objects.base import Property
from plex.objects.directory import Directory
from plex.objects.mixins.session import SessionMixin


class Video(Directory, SessionMixin):
    view_count = Property('viewCount', type=int)
    view_offset = Property('viewOffset', type=int)

    duration = Property(type=int)
