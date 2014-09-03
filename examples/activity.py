import logging
logging.basicConfig(level=logging.DEBUG)

from plex import Plex
from plex.ext.activity import Activity



if __name__ == '__main__':
    ac = Activity()

    @ac.on('websocket.playing')
    def ws_playing(info):
        print "[websocket.playing]", info

    @ac.on('logging.playing')
    def lo_playing(info):
        print "[logging.playing]", info

    ac.start()
