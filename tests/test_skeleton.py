import pytest

from ga_scaffold.skeleton import isqrt, main

__author__ = "Garnik-Arut"
__copyright__ = "Garnik-Arut"
__license__ = "MIT"


def test_fib():
    """API Tests"""
    assert isqrt(1) == 1
    assert isqrt(4) == 0.5
    assert isqrt(16) == 0.25
    # Lets get an error
    with pytest.raises(AssertionError):
        isqrt(-10)


def test_main(capsys):
    """CLI Tests"""
    # capsys is a pytest fixture that allows asserts against stdout/stderr
    # https://docs.pytest.org/en/stable/capture.html
    main(["16"])
    captured = capsys.readouterr()
    assert "The fast inverse square root of 16 is 0.25" in captured.out
