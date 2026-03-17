"""
here i perform a unit test for calculator
using pytest.
"""


# ---------------------------------------------
from calculator import add, subtract, multiply, divide, modulo
# ---------------------------------------------


# calculator test ---------------------

def test_add() -> None:
    assert add(5, 2) == 7


def test_subtract() -> None:
    assert subtract(2, 1) == 1


def test_multiply() -> None:
    assert multiply(10, 5) == 50


def test_divide() -> None:
    assert divide(48, 2) == 24


def test_modulo() -> None:
    assert modulo(10, 4) == 2









