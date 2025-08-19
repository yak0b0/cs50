from seasons import get_date
import pytest


def test_valid_date():
    with pytest.raises(SystemExit):
        get_date("fe")


def test_one_year():
    assert get_date("2024-08-19") != "xd"
