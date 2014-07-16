from plex.objects.base import Descriptor, Property


class Container(Descriptor):
    size = Property(type=int)

    updated_at = Property('updatedAt', int)
