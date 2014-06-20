from plex.objects.base import Descriptor, Property


class Metadata(Descriptor):
    key = Property
    rating_key = Property('ratingKey')

    title = Property
    title_sort = Property('titleSort')
    title_original = Property('originalTitle')

    summary = Property

    thumb = Property

    source_title = Property('sourceTitle')

    added_at = Property('addedAt')
    last_viewed_at = Property('lastViewedAt')
