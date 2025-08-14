import pytest
from working import convert


def test_invalid_input():
    with pytest.raises(ValueError):
        convert("4 PM - 5 PM")


def test_invalid_hour():
    with pytest.raises(ValueError):
        convert("44 AM to 33 PM")


def test_valid_hours():
    assert convert("5 AM to 6 PM") == "05:00 to 18:00"


def test_valid_minutes():
    assert convert("5:05 AM to 6:05 PM") == "05:05 to 18:05"
