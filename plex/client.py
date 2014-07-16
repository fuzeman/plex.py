from plex.interfaces import construct_map
from plex.interfaces.base import InterfaceProxy
from plex.objects.manager import ObjectManager
from plex.request import PlexRequest

import logging
import requests
import socket

log = logging.getLogger(__name__)


class PlexClient(object):
    interfaces = None

    def __init__(self, host='127.0.0.1', port=32400):
        self.base_url = 'http://%s:%s' % (host, port)

        # Construct interfaces
        self.interfaces = construct_map(self)

        # Discover modules
        ObjectManager.construct()

        # Private
        self._session = requests.Session()

    def request(self, path, params=None, data=None, credentials=None, **kwargs):
        log.debug('"%s" - data: %s', path, data)

        request = PlexRequest(
            self,
            path=path,

            params=params,
            data=data,

            credentials=credentials,
            **kwargs
        )

        prepared = request.prepare()

        # TODO retrying requests on 502, 503 errors?

        try:
            return self._session.send(prepared)
        except socket.gaierror, e:
            code, _ = e

            if code != 8:
                raise e

            log.warn('Encountered socket.gaierror (code: 8)')

            return self._rebuild().send(prepared)

    def _rebuild(self):
        log.info('Rebuilding session and connection pools...')

        # Rebuild the connection pool (old pool has stale connections)
        self._session = requests.Session()

        return self._session

    def __getitem__(self, path):
        parts = path.strip('/').split('/')

        cur = self.interfaces

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
