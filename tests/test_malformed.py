from plex import Plex

from tests.core.helpers import read
import responses
import logging

logging.basicConfig(level=logging.DEBUG)


# Set client configuration defaults
Plex.configuration.defaults.server(host='mock')


@responses.activate
def test_detail():
    responses.add(
        responses.GET, 'http://mock:32400',
        body=read('fixtures/detail_malformed.xml'), status=200,
        content_type='application/xml'
    )

    detail = Plex.detail()
    assert detail is None
