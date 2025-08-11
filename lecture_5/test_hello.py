from helo import hello


def test_default():
    assert hello() == "Hello, World"


def test_argument():
    for name in ["John", "Me", "You"]:
        assert hello(name) == f"Hello, {name}"
