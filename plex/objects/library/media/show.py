from plex.objects.base import Property
from plex.objects.directory import Directory
from plex.objects.library.container import Container
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

    def children(self):
        response = self.request('children')

        return self.parse(response, {
            'MediaContainer': (SeasonContainer, {
                'Directory': {
                    'season': 'Season'
                }
            })
        })

    def all_leaves(self):
        response = self.request('allLeaves')

        return self.parse(response, {
            'MediaContainer': ('EpisodeContainer', {
                'Video': {
                    'episode': 'Episode'
                }
            })
        })


class SeasonContainer(Container, Show):
    attribute_map = {
        'index':    'parentIndex',
        'title':    'parentTitle',
        'year':     'parentYear',
        '*':        '*'
    }
