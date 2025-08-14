import pytest
from um import count


def test_uppercase():
    assert count("UM") == 1


def test_um_in_words():
    assert count("yum") == 0


def test_um_with_spaces():
    assert count("um    um   um   ummm ummm um   ") == 4
