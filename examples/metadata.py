import logging
logging.basicConfig(level=logging.DEBUG)

from plex import Plex
from plex.ext.metadata import Matcher, Metadata



if __name__ == '__main__':
    episode = Metadata.get(3)
    print "episode:", episode

    identifier = Matcher.process(episode)
    print "identifier:", identifier
