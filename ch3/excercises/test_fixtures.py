import pytest
import tasks
from tasks import Task

tasks_data = (Task('sleep', done=True),
              Task('wake', 'brian'),
              Task('breathe', 'BRIAN', True),
              Task('exercise', 'BrIaN', False))


@pytest.fixture(params=tasks_data)
def list_of_tasks(tasks_db, request):
    tasks.add(request.param)
    yield
    tasks.delete_all()
