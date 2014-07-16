from plex.objects.base import Descriptor, Property
from plex.objects.library.section import Section


class Metadata(Descriptor):
    section = Property(resolver=lambda: Metadata.construct_section)

    key = Property
    guid = Property
    rating_key = Property('ratingKey')

    title = Property
    title_sort = Property('titleSort')
    title_original = Property('originalTitle')

    summary = Property

    rating = Property(type=float)
    user_rating = Property('userRating', type=float)

    thumb = Property

    source_title = Property('sourceTitle')

    added_at = Property('addedAt')
    last_viewed_at = Property('lastViewedAt')

    @staticmethod
    def construct_section(client, node):
        attribute_map = {
            'key': 'librarySectionID',
            'uuid': 'librarySectionUUID',
            'title': 'librarySectionTitle'
        }

        return Section.construct(client, node, attribute_map, child=True)
