from plex.objects.base import Property
from plex.objects.directory import Directory


class Album(Directory):
    index = Property
    rating_key = Property('ratingKey')

    summary = Property
    year = Property(type=int)

    originally_available_at = Property('originallyAvailableAt')

    leaf_count = Property('leafCount', int)
    viewed_leaf_count = Property('viewedLeafCount', int)

    added_at = Property('addedAt')

    # TODO parent
