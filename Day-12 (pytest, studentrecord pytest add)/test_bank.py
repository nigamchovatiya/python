"""
here i perform a unit test for bankaccount
using pytest.
"""

# -----------------------------------------
from bank import BankAccount
# -----------------------------------------


# BankAccount test ------------------------

def test_deposit() -> None:
    #create BankAccount object
    acc = BankAccount(1500)

    # return final value 2000 test true
    assert acc.deposit(500) == 2000


def test_withdraw() -> None:
    #create BankAccount object
    acc = BankAccount(2000)

    
    assert acc.withdraw(1500) == 500