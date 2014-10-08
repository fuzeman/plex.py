from plex import Plex


for item in Plex['library'].recently_added():
    print '[%s] %s' % (item.type, item.title)
