from plex import Plex

from tests.core.helpers import read
import responses

# Set client configuration defaults
Plex.configuration.defaults.server(host='mock')


@responses.activate
def test_cache():
    http_cache = {}

    # Mock response
    body = read('fixtures/detail_a.xml')

    responses.add_callback(
        responses.GET, 'http://mock:32400/',
        callback=lambda request: (200, {}, body),
        content_type='application/xml'
    )

    with Plex.configuration.cache(http=http_cache):
        # Check initial version retrieval
        assert Plex.version() == "0.9.9.16.555-50cd0c3"

        # Change body, ensure cached version is returned
        body = read('fixtures/detail_b.xml')

        assert Plex.version() == "0.9.9.16.555-50cd0c3"

        # Clear cache, ensure version has changed
        http_cache.clear()

        assert Plex.version() == "0.9.9.14.531-7eef8c6"
