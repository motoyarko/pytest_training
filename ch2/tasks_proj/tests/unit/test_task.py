from collections import namedtuple
import pytest
from tasks import Task


def test_asdict():
    """_asdict() should return a dictionary."""
    t_task = Task('do something', 'okken', True, 21)
    t_dict = t_task._asdict()
    expected = {'summary': 'do something', 'owner': 'okken', 'done': True, 'id': 21}
    assert t_dict == expected


@pytest.mark.run_these_please
def test_replace():
    """replace() should change passed in fields."""
    t_before = Task('finish book', 'brain', False)
    t_after = t_before._replace(id=10, done=True)
    t_expected = Task('finish book', 'brain', True, 10)
    assert t_after == t_expected


def test_defaults():
    t1 = Task()
    t2 = Task(None, None, False, None)
    assert t1 == t2


@pytest.mark.run_these_please
def test_member_access():
    t = Task('buy milk', 'brain')
    assert t.summary == 'buy milk'
    assert t.owner in 'brain1111'
    assert (t.done, t.id) == (False, None)