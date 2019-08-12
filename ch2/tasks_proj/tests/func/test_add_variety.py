import pytest
import tasks
from tasks import Task

tasks_to_try = Task('sleep', done=True), Task('wake', 'brian'), Task('breathe', 'BRIAN', True), Task('exercise', 'BrIaN', False)
task_ids = ['Task({}, {}, {})'.format(t.summary, t.owner, t.done) for t in tasks_to_try]


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


@pytest.mark.parametrize('summary, owner, done', [('sleep', None, False), ('wake', 'brian', False), ('breathe', 'BRIAN', True), ('eat eggs', 'BrIaN', False)])
def test_add_3(summary, owner, done):
    """parametrize with multiple params"""
    task = Task(summary, owner, done)
    task_id = tasks.add(task)
    t_from_db = tasks.get(task_id)
    assert equivalent(task, t_from_db)


@pytest.mark.parametrize('task', tasks_to_try)
def test_add_4(task):
    """get tasks from variable"""
    task_id = tasks.add(task)
    t_from_db = tasks.get(task_id)
    assert equivalent(t_from_db, task)


@pytest.mark.parametrize('task', tasks_to_try, ids=task_ids)
def test_add_5(task):
    """Demonstrate ids."""
    task_id = tasks.add(task)
    t_from_db = tasks.get(task_id)
    assert equivalent(t_from_db, task)


@pytest.mark.parametrize('task', [pytest.param(Task('create'), id='summary'),
                                  pytest.param(Task('create', 'Michelle'), id='summary/owner'),
                                  pytest.param(Task('create', 'Michelle', True), id='summary/owner/done')])
def test_add_6(task):
    """pytest.param and id"""
    task_id = tasks.add(task)
    t_from_db = tasks.get(task_id)
    assert equivalent(t_from_db, task)


@pytest.mark.parametrize('task', tasks_to_try, ids=task_ids)
def test_check_count_after_add(task):
    """check count and """
    count_before = tasks.count()
    tasks.add(task)
    count_after = tasks.count()
    assert (count_before + 1) == count_after


@pytest.mark.parametrize('task', tasks_to_try, ids=task_ids)
class TestAdd():
    """Demonstrate parametrize and test classes."""

    def test_equivalent(self, task):
        task_id = tasks.add(task)
        t_from_db = tasks.get(task_id)
        assert equivalent(t_from_db, task)

    def test_valid_id(self, task):
        task_id = tasks.add(task)
        t_from_db = tasks.get(task_id)
        assert t_from_db.id == task_id
