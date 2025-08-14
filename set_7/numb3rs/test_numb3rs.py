import pytest
from numb3rs import validate


def test_string():
    assert validate("cat") == False


def test_leading_zero():
    assert validate("0.0.0.0") == False


def test_leading_zero():
    assert validate("0.0.0.1") == True


def test_too_much():
    assert validate("600.5.34.23") == False
    assert validate("256.3.4.5") == False
    assert validate("256.256.256.256") == False


def test_too_long():
    assert validate("233.233.233.233.233") == False


def test_first_byte_in_range():
    assert validate("-32.354.32.211") == False
    assert validate("32.122.232.121") == True
    assert validate("9999999999999.6.6.6") == False
    assert validate("64.126.256.512") == False


def test_xd():
    assert validate(
        "9999999999.999999999999.9999999999999.9999999999999") == False
