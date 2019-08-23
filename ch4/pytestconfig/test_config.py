import pytest


def test_option(pytestconfig):
    print('"foo" set to:', pytestconfig.getoption('foo'))
    print('"myopt" set to', pytestconfig.getoption('myopt'))


@pytest.fixture()
def foo(pytestconfig):
    return pytestconfig.option.foo


@pytest.fixture()
def myopt(pytestconfig):
    return pytestconfig.option.myopt


def test_fixtures_for_options(foo, myopt):
    print('"myopt" is:', myopt)
    print(('"foo" is:', foo))
