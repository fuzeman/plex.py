from plex.objects.base import Property
from plex.objects.library.media.show import Show
from plex.objects.library.metadata import Metadata
from plex.objects.library.video import Directory


class Season(Directory, Metadata):
    show = Property(resolver=lambda: Season.construct_show)

    index = Property

    episode_count = Property('leafCount', int)
    viewed_episode_count = Property('viewedLeafCount', int)


    @staticmethod
    def construct_show(client, node):
        attribute_map = {
            'index':     'parentIndex',
            'key':       'parentKey',
            'ratingKey': 'parentRatingKey',

            'title':     'parentTitle',
            'summary':   'parentSummary',
            'thumb':     'parentThumb',

            'theme':     'parentTheme'
        }

        return attribute_map.values(), Show.construct(client, node, attribute_map)
