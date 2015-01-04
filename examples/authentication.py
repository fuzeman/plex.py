from plex import Plex

token = raw_input('Authentication token: ')


with Plex.configuration.authentication(token):
    recently_added = Plex['library'].recently_added()

    for item in recently_added:
        print '[%s] %s' % (item.type, item.title)
