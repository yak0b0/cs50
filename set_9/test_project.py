import pytest
from project import is_currency_valid, convert_amount_by_rate


def test_empty_currency():
    with pytest.raises(ValueError):
        is_currency_valid("", {"GBP", "PLN"})


def test_invalid_currency():
    with pytest.raises(ValueError):
        is_currency_valid("GBPP", {"GBP", "PLN"})


def test_valid_currency():
    assert is_currency_valid("GBP", {"GBP", "PLN"}) == True


def test_lowercase_currency():
    assert is_currency_valid("gbp", {"GBP", "PLN"}) == True


def test_invalid_ammount():
    with pytest.raises(ValueError):
        convert_amount_by_rate(-4, 3)
        convert_amount_by_rate("pig", 3)
