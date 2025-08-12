import pytest

from twttr import shorten


def test_word_no_vowel():
    assert shorten("nthg") == "nthg"


def test_word_with_vowel():
    assert shorten("nothing") == "nthng"


def test_number():
    assert shorten("iii4") == "4"


def test_cap_vowel():
    assert shorten("NOthING") == "NthNG"


def test_punct():
    assert shorten("hi, how are you") == "h, hw r y"
