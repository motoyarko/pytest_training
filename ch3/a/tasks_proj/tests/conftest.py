import pytest
import tasks
from tasks import Task


@pytest.fixture(scope='session', params=['tiny',])
#@pytest.fixture(scope='session', params=['tiny', 'mongo'])
def tasks_db_session(tmpdir_factory, request):
    """Connect to db before tests, disconnect after."""
    temp_dir = tmpdir_factory.mktemp('temp')
    tasks.start_tasks_db(str(temp_dir), request.param)
    yield
    tasks.stop_tasks_db()


@pytest.fixture()
def tasks_db(tasks_db_session):
    """an empty tasks db"""
    tasks.delete_all()


# Reminder of Task constructor interface
# Task(summary=None, owner=None, done=False, id=None)
# summary is required
# owner and done are optional
# id is set by database


@pytest.fixture(scope='session')
def tasks_just_a_few():
    """all summaries and owners are required"""
    return (
        Task('Write some code', 'Brian', True),
        Task("Code review Brian's code", 'Katie', False),
        Task('Fix what Brian did', 'Michelle', False)
    )


@pytest.fixture(scope='session')
def tasks_mult_per_owner():
    """several owners with several tasks each"""
    return (
        Task('Make a cookie', 'Raphael'),
        Task('Use an emoji', 'Raphael'),
        Task('Move to Berlin', 'Raphael'),

        Task('Create', 'Michelle'),
        Task('Inspire', 'Michelle'),
        Task('Encourage', 'Michelle'),

        Task('Do a handstand', 'Daniel'),
        Task('Write some books', 'Daniel'),
        Task('Eat ice cream', 'Daniel')
    )


@pytest.fixture()
def db_with_3_tasks(tasks_db, tasks_just_a_few):
    """Connected db with 3 tasks, all unique."""
    for t in tasks_just_a_few:
        tasks.add(t)


@pytest.fixture()
def db_with_multi_per_one_owner(tasks_db, tasks_mult_per_owner):
    """Connected db with 9 tasks, 3 owners, all with 3 tasks."""
    for t in tasks_mult_per_owner:
        tasks.add(t)


# @pytest.fixture(autouse=True)
# def check_duration(request, cache):
#     key = 'duration/' + request.node.nodeid.replace(':', '_')
#     # nodeid's can have colons
#     # keys become filenames within .cache
#     # replace colons with something filename safe
#     start_time = datetime.datetime.now()
#     yield
#     stop_time = datetime.datetime.now()
#     this_duration = (stop_time - start_time).total_seconds()
#     last_duration = cache.get(key, None)
#     cache.set(key, this_duration)
#     if last_duration is not None:
#         errorstring = "test duration over 2x last duration"
#         assert this_duration <= last_duration * 2, errorstring