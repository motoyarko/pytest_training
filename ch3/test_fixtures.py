import pytest


@pytest.fixture()
def some_data():
    """return answer"""
    return 42


def test_some_data(some_data):
    """use fixture value in a test"""
    assert some_data == 42

