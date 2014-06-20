from plex.objects.base import Descriptor, Property


class Metadata(Descriptor):
    # TODO genres
    # TODO tags
    # TODO collections

    duration = Property(type=int)
    rating = Property(type=float)

    title_original = Property('originalTitle')
    title_sort = Property('titleSort')

    key = Property
    rating_key = Property('ratingKey')

    source_title = Property('sourceTitle')
