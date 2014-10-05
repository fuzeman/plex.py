# coding=utf-8

from plex import Plex

from tests.core.helpers import read
import responses

# Set client configuration defaults
Plex.configuration.defaults.server(host='mock')


@responses.activate
def test_recently_added():
    responses.add(
        responses.GET, 'http://mock:32400/library/recentlyAdded',
        body=read('fixtures/library/recently_added.xml'), status=200,
        content_type='application/xml'
    )

    container = Plex['library'].recently_added()
    assert container is not None

    items = list(container)
    assert len(items) == 3

    # Validate 'movie'
    assert items[0].type == 'movie'
    assert items[0].title == "TRON: Legacy"
    assert items[0].year == 2010

    assert items[0].director.tag == "Joseph Kosinski"
    assert items[0].country.tag == "USA"

    assert [genre.tag for genre in items[0].genres] == [
        "Action",
        "Adventure"
    ]

    assert [writer.tag for writer in items[0].writers] == [
        "Adam Horowitz",
        "Richard Jefferies"
    ]

    assert [role.tag for role in items[0].roles] == [
        "Garrett Hedlund",
        "Jeff Bridges",
        "Olivia Wilde"
    ]

    # Validate 'season'
    assert items[1].type == 'season'
    assert items[1].title == "Specials"
    assert items[1].index == 0

    assert items[1].show.title == "Gold Rush"
    assert items[1].show.index == 1

    # Validate 'album'
    assert items[2].type == 'album'
    assert items[2].title == "Angel Milk"
    assert items[2].index == 1

    assert items[2].artist.title == u"Télépopmusik"

    assert [genre.tag for genre in items[2].genres] == [
        "Electronic",
        "Electronica"
    ]


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
