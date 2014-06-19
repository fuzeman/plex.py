from plex.interfaces.base import Interface
from plex.objects.library.container import Container
from plex.objects.library.section import Section


class LibraryInterface(Interface):
    path = 'library'

    def metadata(self, rating_key):
        return self.request('metadata', rating_key)

    def on_deck(self):
        raise NotImplementedError()

    def recently_added(self):
        return self.request('recentlyAdded')

    def sections(self):
        response = self.request('sections')

        return self.parse(response, {
            'MediaContainer': (Container, {
                'Directory': Section
            })
        })
