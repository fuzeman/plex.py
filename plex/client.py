from plex.interfaces import construct_map
from plex.interfaces.core.base import InterfaceProxy
from plex.objects.core.manager import ObjectManager
from plex.request import PlexRequest

import logging
import requests
import socket

log = logging.getLogger(__name__)


class PlexClient(object):
    __interfaces = None

    def __init__(self, host='127.0.0.1', port=32400):
        self.base_url = 'http://%s:%s' % (host, port)

        # Construct interfaces
        self.__interfaces = construct_map(self)

        # Discover modules
        ObjectManager.construct()

        # Private
        self.__session = requests.Session()

    def _request(self, path, params=None, query=None, data=None, credentials=None, **kwargs):
        request = PlexRequest(
            self,
            path=path,

            params=params,
            query=query,
            data=data,

            credentials=credentials,
            **kwargs
        )

        prepared = request.prepare()

        log.debug('%s %s - data: %s', prepared.method, prepared.path_url, data)

        # TODO retrying requests on 502, 503 errors?

        try:
            return self.__session.send(prepared)
        except socket.gaierror, e:
            code, _ = e

            if code != 8:
                raise e

            log.warn('Encountered socket.gaierror (code: 8)')

            return self._rebuild().send(prepared)

    def _rebuild(self):
        log.info('Rebuilding session and connection pools...')

        # Rebuild the connection pool (old pool has stale connections)
        self.__session = requests.Session()

        return self.__session

    def __getitem__(self, path):
        parts = path.strip('/').split('/')

        cur = self.__interfaces

        while parts and type(cur) is dict:
            key = parts.pop(0)

            if key not in cur:
                return None

            cur = cur[key]

        if type(cur) is dict:
            cur = cur.get(None)

        if parts:
            return InterfaceProxy(cur, parts)

        return cur

    def __getattr__(self, name):
        interface = self.__interfaces.get(None)

        if not interface:
            raise Exception("Root interface not found")

        return getattr(interface, name)
