def pytest_addoption(parser):
    parser.addoption("--myopt", action="store_true", default="none", help="some boolean option")
    parser.addoption("--foo", action="store", default="bar", help="foo: bar on baz")