from plex import Plex


with Plex.configuration.server(host='192.168.1.110'):
    recently_added = Plex['library'].recently_added()

    for item in recently_added:
        print '[%s] %s' % (item.type, item.title)
