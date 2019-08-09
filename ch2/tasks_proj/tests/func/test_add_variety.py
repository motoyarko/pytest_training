import pytest
import tasks
from tasks import Task


@pytest.fixture(autouse=True)
def initialized_tasks_db(tmpdir):
    """Connect to db before testing, disconnect after."""
    # Setup : start db
    tasks.start_tasks_db(str(tmpdir), 'tiny')
    yield  # this is where the testing happens
    # Teardown : stop db
    tasks.stop_tasks_db()


def equivalent(t1, t2):
    """Compare tasks"""
    return (t1.summary == t2.summary) and (t1.owner == t2.owner) and (t1.done == t2.done)


def test_add_1():
    """tasks.get() using id returned from add() works."""
    task = Task('breathe', 'BRAIN', True)
    task_id = tasks.add(task)
    t_from_db = tasks.get(task_id)
    #  id should be the same
    assert equivalent(t_from_db, task)


@pytest.mark.parametrize('task', [Task('sleep', done=True), Task('wake', 'brian'), Task('breathe', 'BRIAN', True), Task('exercise', 'BrIaN', False)])
def test_add_2(task):
    """parametrize with one param"""
    task_id = tasks.add(task)
    t_from_db = tasks.get(task_id)
    assert equivalent(task, t_from_db)
