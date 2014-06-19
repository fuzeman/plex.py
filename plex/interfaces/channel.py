from plex.interfaces.base import Interface


class ChannelInterface(Interface):
    path = 'channels'

    def all(self):
        raise NotImplementedError()
