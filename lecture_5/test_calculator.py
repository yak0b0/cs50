from calculator import square
import pytest

# def main():
#    test_square_2()
#


def test_positive():
    assert square(2) == 4
    assert square(3) == 9


def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9


def test_zero():
    assert square(0) == 0


def test_str():
    with pytest.raises(TypeError):
        square("cat")

# unit tests, are test for values


# def test_square():
#    try:
#        assert square(2) == 4
#        assert square(3) == 9
#   except AssertionError:
#        print("The square function is not built correctly")


# if __name__ == "__main__":
#    main()

# assert (to boldly claim something is true)
