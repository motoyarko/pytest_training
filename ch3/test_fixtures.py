import pytest


@pytest.fixture()
def some_data():
    """return answer"""
    return 42


@pytest.fixture()
def a_tuple():
    """Return something more interesting."""
    return (1, 'foo', None, {'bar': 23})


def test_some_data(some_data):
    """use fixture value in a test"""
    assert some_data == 42


def test_a_tuple(a_tuple):
    """Demo for a_tuple fixture"""
    assert a_tuple[3]['bar'] == 32

