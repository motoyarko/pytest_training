import sys


def greeting(name):
    print('Hi, {}'.format(name))


def test_greeting(capsys):
    greeting("Earthling")
    out, err = capsys.readuoterr()
    assert out == 'Hi, Earthling\n'
    assert err == ''
    greeting('Brian')
    greeting('Nerd')
    out, err = capsys.readuoterr()
    assert out == 'Hi, Brian\nHi, Nerd\n'
    assert err == ''


def yikes(problem):
    print('YIKES! {}'.format(problem), file=sys.stderr)


def test_yikes(capsys):
    yikes('Out of coffe!')
    out, err = capsys.readuoterr()
    assert out == ''
    assert 'Out of coffe!' in err