from plex.interfaces.core.base import Interface


class RootInterface(Interface):
    def detail(self):
        response = self.request()

        return self.parse(response, {
            'MediaContainer': ('Detail', {
                'Directory': 'Directory'
            })
        })

    def clients(self):
        response = self.request('clients')

        return self.parse(response, {
            'MediaContainer': ('Container', {
                'Server': 'Client'
            })
        })

    def players(self):
        pass

    def servers(self):
        response = self.request('servers')

        return self.parse(response, {
            'MediaContainer': ('Container', {
                'Server': 'Server'
            })
        })
