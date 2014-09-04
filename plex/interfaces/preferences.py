from plex.interfaces.core.base import Interface


class PreferencesInterface(Interface):
    path = ':/prefs'

    def get(self, id=None):
        response = self.http.get()

        container = self.parse(response, {
            'MediaContainer': ('MediaContainer', {
                'Setting': 'Setting'
            })
        })

        if id is None:
            return container

        for setting in container:
            if setting.id == id:
                return setting

        return None

    def set(self, id, value):
        pass
