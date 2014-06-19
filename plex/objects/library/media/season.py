from plex.objects.base import Property
from plex.objects.library.video import Directory


class Season(Directory):
    index = Property
    rating_key = Property('ratingKey')

    summary = Property

    leaf_count = Property('leafCount', int)
    viewed_leaf_count = Property('viewedLeafCount', int)

    added_at = Property('addedAt')
    last_viewed_at = Property('lastViewedAt')
