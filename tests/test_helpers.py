from plex.core.helpers import to_iterable


def test_to_iterable():
    assert to_iterable(None) is None
    assert to_iterable("test") == ["test"]

    assert to_iterable(100) == [100]
    assert to_iterable([100]) == [100]
    assert to_iterable([]) == []

    assert to_iterable((100,)) == (100,)
    assert to_iterable(tuple([])) == tuple([])
