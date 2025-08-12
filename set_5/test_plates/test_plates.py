from plates import is_valid
import pytest


def test_length():
    assert is_valid("SEVENSS") == False


def test_first_alphabet():
    assert is_valid("111111") == False


def test_zero():
    assert is_valid("DF0") == False


def test_number_placement():
    assert is_valid("AAA22A") == False
    assert is_valid("AAA222") == True


def test_alphanumeric():
    assert is_valid("FD,D") == False
