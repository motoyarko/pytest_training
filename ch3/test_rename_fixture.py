"""fixture renaming demonstration"""

import pytest


@pytest.fixture(name='lue')
def ultimate_answer_to_life_the_universe_and_everything():
    """return answer"""
    return 42


def test_everything(lue):
    """use shorter name"""
    assert lue == 42
