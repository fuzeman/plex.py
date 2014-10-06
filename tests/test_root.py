from plex import Plex

from tests.core.helpers import read
import responses

# Set client configuration defaults
Plex.configuration.defaults.server(host='mock')


@responses.activate
def test_detail():
    responses.add(
        responses.GET, 'http://mock:32400',
        body=read('fixtures/detail.xml'), status=200,
        content_type='application/xml'
    )

    detail = Plex.detail()
    assert detail is not None

    assert detail.friendly_name == "Mock Server"

    assert detail.platform == "Windows"
    assert detail.platform_version == "6.2 (Build 9200)"


@responses.activate
def test_version():
    responses.add(
        responses.GET, 'http://mock:32400',
        body=read('fixtures/detail.xml'), status=200,
        content_type='application/xml'
    )

    version = Plex.version()

    assert version == "0.9.9.16.555-50cd0c3"


@responses.activate
def test_clients():
    responses.add(
        responses.GET, 'http://mock:32400/clients',
        body=read('fixtures/clients.xml'), status=200,
        content_type='application/xml'
    )

    container = Plex.clients()
    assert container is not None

    items = list(container)
    assert len(items) == 1

    assert items[0].name == "One"
    assert items[0].address == "192.168.1.100"
    assert items[0].version == "1.2.2.331-2d6426d7"

    assert items[0].protocol_capabilities == "navigation,playback,timeline,mirror,playqueues"


@responses.activate
def test_clients_filter():
    responses.add(
        responses.GET, 'http://mock:32400/clients',
        body=read('fixtures/clients.xml'), status=200,
        content_type='application/xml'
    )

    container = Plex.clients()
    assert container is not None

    items = list(container.filter(["a7d1b50a-42d1-40b5-9db6-6b0afd013438"]))
    assert len(items) == 1

    assert items[0].machine_identifier == "a7d1b50a-42d1-40b5-9db6-6b0afd013438"


@responses.activate
def test_clients_get():
    responses.add(
        responses.GET, 'http://mock:32400/clients',
        body=read('fixtures/clients.xml'), status=200,
        content_type='application/xml'
    )

    container = Plex.clients()
    assert container is not None

    # Try retrieve item that exists
    item = container.get("a7d1b50a-42d1-40b5-9db6-6b0afd013438")
    assert item is not None

    assert item.machine_identifier == "a7d1b50a-42d1-40b5-9db6-6b0afd013438"

    # Try retrieve item that doesn't exist
    item = container.get("invalid-identifier")
    assert item is None


@responses.activate
def test_servers():
    responses.add(
        responses.GET, 'http://mock:32400/servers',
        body=read('fixtures/servers.xml'), status=200,
        content_type='application/xml'
    )

    container = Plex.servers()
    assert container is not None

    items = list(container)
    assert len(items) == 2

    assert items[0].name == "One"
    assert items[0].address == "192.168.1.100"
    assert items[0].version == "0.9.9.16.555-50cd0c3"

    assert items[1].name == "Two"
    assert items[1].address == "192.168.1.101"
    assert items[1].version == "0.9.9.14.531-7eef8c6"
