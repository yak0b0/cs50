from bank import value
import pytest


def test_greeting_with_hello_lower():
    assert value("hello") == 0


def test_greeting_with_hello_upper():
    assert value("HELLO") == 0


def test_greeting_with_hello_r():
    assert value("HEllO") == 0


def test_greeting_h_lower():
    assert value("hi") == 20


def test_greeting_h_upper():
    assert value("HI") == 20


def test_greeting_h_r():
    assert value("hI") == 20


def test_no_h():
    assert value("yo, wagwan") == 100
