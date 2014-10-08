from plex import Plex
from plex.serializer import Serializer

from tests.core.helpers import read
import responses

# Set client configuration defaults
Plex.configuration.defaults.server(host='mock')


@responses.activate
def test_metadata():
    responses.add(
        responses.GET, 'http://mock:32400/library/metadata/31',
        body=read('fixtures/library/metadata/episode.xml'), status=200,
        content_type='application/xml'
    )

    # Retrieve mock [Episode] object
    container = Plex['library'].metadata(31)
    assert container is not None

    items = list(container)
    assert len(items) == 1

    # Encode item
    encoded = Serializer.encode(items[0])
    assert encoded

    # Decode item
    decoded = Serializer.decode(encoded, Plex.client)
    assert decoded

    # Basic property check
    assert decoded.title == items[0].title
    assert decoded.guid == items[0].guid
