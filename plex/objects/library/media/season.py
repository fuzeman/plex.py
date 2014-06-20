from plex.objects.base import Property
from plex.objects.library.metadata import Metadata
from plex.objects.library.video import Directory


class Season(Directory, Metadata):
    index = Property

    episode_count = Property('leafCount', int)
    viewed_episode_count = Property('viewedLeafCount', int)
