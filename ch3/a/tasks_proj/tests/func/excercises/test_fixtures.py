import pytest
import tasks
from tasks import Task

tasks_data = (Task('sleep', done=True),
              Task('wake', 'brian'),
              Task('breathe', 'BRIAN', True),
              Task('exercise', 'BrIaN', False))


def equivalent(t1, t2):
    """Check two tasks for equivalence."""
    return (t1.summary == t2.summary) and (t1.owner == t2.owner) and (t1.done == t2.done)


@pytest.fixture(params=tasks_data)
def list_of_tasks(request):
    print('\n' + str(request.param.owner))
    yield request.param
    print('\n' + str(request.param.owner))


def test_my_fixture(list_of_tasks, tasks_db):
    id1 = tasks.add(list_of_tasks)
    t1 = tasks.get(id1)
    assert equivalent(t1, list_of_tasks)
