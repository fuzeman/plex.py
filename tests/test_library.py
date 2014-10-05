from plex import Plex

from tests.core.helpers import read
import responses

# Set client configuration defaults
Plex.configuration.defaults.server(host='mock')


@responses.activate
def test_metadata_episode():
    responses.add(
        responses.GET, 'http://mock:32400/library/metadata/31',
        body=read('fixtures/library/metadata/episode.xml'), status=200,
        content_type='application/xml'
    )

    container = Plex['library'].metadata(31)
    assert container is not None

    items = list(container)
    assert len(items) == 1

    episode = items[0]

    # - index
    assert episode.index == 1
    assert episode.season.index == 6

    # - title
    assert episode.title == "London (1)"
    assert episode.show.title == "Parks and Recreation"

    # - writer
    assert "Michael Schur" in [wr.tag for wr in episode.writers]

    # - director
    assert episode.director.tag == "Dean Holland"

    # - guid
    assert episode.guid == "com.plexapp.agents.thetvdb://84912/6/1?lang=en"


@responses.activate
def test_all_leaves_show():
    responses.add(
        responses.GET, 'http://mock:32400/library/metadata/1/allLeaves',
        body=read('fixtures/library/all_leaves/show.xml'), status=200,
        content_type='application/xml'
    )

    container = Plex['library/metadata'].all_leaves(1)
    assert container is not None

    items = list(container)
    assert len(items) == 6

    # Ensure season/episode indexes are correct
    assert [(episode.season.index, episode.index) for episode in items] == [
        (10, 1), (10, 2),
        (11, 1), (11, 2),
        (12, 1), (12, 2)
    ]
