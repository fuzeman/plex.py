from plex import Plex

from tests.core.helpers import read
import responses

# Set client configuration defaults
Plex.configuration.defaults.server(host='mock')


@responses.activate
def test_get_all():
    responses.add(
        responses.GET, 'http://mock:32400/:/prefs',
        body=read('fixtures/prefs.xml'), status=200,
        content_type='application/xml'
    )

    container = Plex[':/prefs'].get()
    assert container is not None

    items = list(container)
    assert len(items) == 3

    # Validate preferences
    assert items[0].id == "FriendlyName"
    assert items[0].group == 'general'

    assert items[1].id == "collectUsageData"
    assert items[1].group == 'general'

    assert items[2].id == "FSEventLibraryUpdatesEnabled"
    assert items[2].group == 'library'


@responses.activate
def test_get_single():
    responses.add(
        responses.GET, 'http://mock:32400/:/prefs',
        body=read('fixtures/prefs.xml'), status=200,
        content_type='application/xml'
    )

    item = Plex[':/prefs'].get('FriendlyName')
    assert item is not None

    # Validate preferences
    assert item.id == "FriendlyName"
    assert item.group == 'general'


@responses.activate
def test_set():
    responses.add(
        responses.PUT, 'http://mock:32400/:/prefs',
        body='', status=200,
        content_type='application/xml'
    )

    Plex[':/prefs'].set('FriendlyName', 'Mock Server')

    assert len(responses.calls) == 1
