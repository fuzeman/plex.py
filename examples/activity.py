import logging
logging.basicConfig(level=logging.DEBUG)

from plex import Plex
from plex.ext.activity import Activity



if __name__ == '__main__':
    ac = Activity(
        sources=['websocket']
    )

    @ac.on('notification.playing')
    def on_playing(info):
        print 'on_playing', info

    ac.start()
