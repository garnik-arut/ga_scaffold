import pytest

from ga_scaffold.skeleton import isqrt, main

__author__ = "Garnik-Arut"
__copyright__ = "Garnik-Arut"
__license__ = "MIT"


def rounded_compare(a, b, decimals=0):
    return round(a, decimals) == round(b, decimals)


def test_isqrt():
    """API Tests"""
    assert rounded_compare(isqrt(1 / 16), 4)
    assert rounded_compare(isqrt(0.25), 2)
    # Lets get an error
    with pytest.raises(AssertionError):
        isqrt(-10)


def test_main(capsys):
    """CLI Tests"""
    # capsys is a pytest fixture that allows asserts against stdout/stderr
    # https://docs.pytest.org/en/stable/capture.html
    main(["100"])
    captured = capsys.readouterr()
    assert "The fast inverse square root of 100 is 0.099" in captured.out
