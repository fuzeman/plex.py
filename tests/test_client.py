from plex import Plex

from tests.core.helpers import read
import pytest
import responses

# Set client configuration defaults
Plex.configuration.defaults.server(host='mock')


@responses.activate
def test_interface_proxy():
    responses.add(
        responses.GET, 'http://mock:32400/library/metadata/1/allLeaves',
        body=read('fixtures/library/all_leaves/show.xml'), status=200,
        content_type='application/xml'
    )

    container = Plex['library/metadata/1'].all_leaves()
    assert container is not None

    items = list(container)
    assert len(items) == 6


@responses.activate
def test_interface_getitem():
    interface = Plex['library/metadata']

    # Ensure all_leaves() method is returned
    assert interface['all_leaves']

    # Ensure exception is raised when a method is missing
    with pytest.raises(ValueError):
        m = interface['missing']
