from plex import Plex

from tests.core.helpers import read
import responses

# Set client configuration defaults
Plex.configuration.defaults.server(host='mock')


@responses.activate
def test_sections():
    responses.add(
        responses.GET, 'http://mock:32400/library/sections',
        body=read('fixtures/library/sections.xml'), status=200,
        content_type='application/xml'
    )

    container = Plex['library'].sections()
    assert container is not None

    items = list(container)
    assert len(items) == 2

    # Validate sections
    assert items[0].type == 'show'
    assert items[0].agent == 'com.plexapp.agents.thetvdb'

    assert items[1].type == 'movie'
    assert items[1].agent == 'com.plexapp.agents.themoviedb'
