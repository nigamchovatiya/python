"""
here i perform a pytest in math.py file
"""

# ----------------------------------------
from math_utils import add
# ----------------------------------------


def test_add() -> None:
    result = add(2, 3)
    # assert check result 
    # result 5 -- pass
    # result not 5 -- fail
    assert result == 5 
