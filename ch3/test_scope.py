"""DEmo fixture scope"""

import pytest


@pytest.fixture(scope='function')
def func_scope():
    """Function scope fixture"""


@pytest.fixture(scope='module')
def mod_scope():
    """module scope fixture"""


@pytest.fixture(scope='session')
def sess_scope():
    """session scope fixture"""


@pytest.fixture(scope='class')
def class_scope():
    """class scope fixture"""


def test_1(sess_scope, mod_scope, func_scope):
    """Test using session, module, and function scope fixtures"""


def test_2(sess_scope, mod_scope, func_scope):
    """second test with session, module, and function scope fixtures"""


@pytest.mark.usefixtures('class_scope')
class TestSomething:
    """Demo class scope fixtures."""

    def test_3(self):
        """Test using a class scope fixture."""

    def test_4(self):
        """Second Test using a class scope fixture."""
