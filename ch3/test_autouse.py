""" autouse demonstration"""

import pytest
import time


@pytest.fixture(autouse=True, scope='session')
def footer_session_scope():
    """report time at the end of session"""
    yield
    now = time.time()
    print('--')
    print('finished : {}'.format(time.strftime('%d %b %X', time.localtime(now))))
    print('--------------')


@pytest.fixture(autouse=True)
def footer_function_scope():
    """report test durations after each scope"""
    start = time.time()
    yield
    stop = time.time()
    delta = stop - start
    print('\ntest duration : {:0.3} seconds'.format(delta))


def test_1():
    """simulate long test"""
    time.sleep(1)


def test_2():
    """simulate longer test"""
    time.sleep(1.23)
