from plex.objects.base import Descriptor, Property
from plex.objects.library.section import Section


class Container(Descriptor):
    section = Property(resolver=lambda: Container.construct_section)

    title1 = Property
    title2 = Property

    identifier = Property
    size = Property(type=int)

    view_group = Property('viewGroup')
    view_mode = Property('viewMode', int)

    media_tag_prefix = Property('mediaTagPrefix')
    media_tag_version = Property('mediaTagVersion')

    no_cache = Property('nocache', bool)
    allow_sync = Property('allowSync', bool)
    mixed_parents = Property('mixedParents', bool)

    @staticmethod
    def construct_section(client, node):
        attribute_map = {
            'key': 'librarySectionID',
            'uuid': 'librarySectionUUID',
            'title': 'librarySectionTitle'
        }

        return attribute_map.values(), Section.construct(client, node, attribute_map, child=True)
