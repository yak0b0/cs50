from fuel import gauge
from fuel import convert
import pytest


def test_int():
    assert convert("3/4") == 75


def test_value_error():
    with pytest.raises(ValueError):
        convert("4/3")


def test_negative_value_error():
    with pytest.raises(ValueError):
        convert("-3/3")


def test_zero_division_error():
    with pytest.raises(ZeroDivisionError):
        convert("2/0")


def test_empty_output():
    assert gauge(1) == "E"


def test_full_output():
    assert gauge(99) == "F"


def test_normal_output():
    assert gauge(69) == "69%"
