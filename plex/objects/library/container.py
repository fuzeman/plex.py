from plex.objects.base import Descriptor, Property


class Container(Descriptor):
    identifier = Property
    size = Property(type=int)

    media_tag_prefix = Property('mediaTagPrefix')
    media_tag_version = Property('mediaTagVersion')

    allow_sync = Property('allowSync', bool)
    mixed_parents = Property('mixedParents', bool)
