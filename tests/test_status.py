# coding=utf-8

from plex import Plex

from tests.core.helpers import read
import responses

# Set client configuration defaults
Plex.configuration.defaults.server(host='mock')


@responses.activate
def test_sessions():
    responses.add(
        responses.GET, 'http://mock:32400/status/sessions',
        body=read('fixtures/status/sessions.xml'), status=200,
        content_type='application/xml'
    )

    container = Plex['status'].sessions()
    assert container is not None

    items = list(container)
    assert len(items) == 3

    # Validate 'episode'
    assert items[0].title == "Blind Date"
    assert items[0].type == 'episode'

    assert items[0].show.title == "30 Rock"

    assert items[0].session.key == 3
    assert items[2].session.player.title == "One"
    assert items[2].session.user.title == "someone"

    # Validate 'movie'
    assert items[1].title == "The Hobbit The Desolation of Smaug"
    assert items[1].type == 'movie'

    assert items[1].session.key == 5
    assert items[2].session.player.title == "One"
    assert items[2].session.user.title == "someone"

    # Validate 'track'
    assert items[2].title == "Don't look back"
    assert items[2].type == 'track'

    assert items[2].album.title == "Angel Milk"
    assert items[2].artist.title == u"Télépopmusik"

    assert items[2].session.key == 4
    assert items[2].session.player.title == "One"
    assert items[2].session.user.title == "someone"
