from plex.objects.base import Property
from plex.objects.directory import Directory
from plex.objects.library.metadata import Metadata


class Show(Directory, Metadata):
    index = Property
    duration = Property(type=int)

    studio = Property
    content_rating = Property('contentRating')

    banner = Property
    theme = Property

    year = Property(type=int)
    originally_available_at = Property('originallyAvailableAt')

    episode_count = Property('leafCount', int)
    viewed_episode_count = Property('viewedLeafCount', int)
