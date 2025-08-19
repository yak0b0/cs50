import pytest
from jar import Jar


def test_init():
    jar = Jar()
    assert jar.capacity == 12


def test_str():
    har = Jar()
    har.deposit(4)
    assert print(har) == print("🍪" * 4)


def test_deposit():
    bar = Jar()
    bar.deposit(2)
    assert bar.size == 2
    with pytest.raises(ValueError):
        bar.deposit(11)


def test_withdraw():
    aar = Jar()
    aar.deposit(11)
    aar.withdraw(2)
    assert aar.size == 9
    with pytest.raises(ValueError):
        aar.withdraw(11)
