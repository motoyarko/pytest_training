import tasks


def test_my_fixture(list_of_tasks):
    t1 = tasks.get(1)
    assert t1 is not None
