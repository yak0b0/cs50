from helo import hello


def test_default():
    assert hello() == "Hello, World"


def test_argument():
    assert hello("You") == "Hello, You"
