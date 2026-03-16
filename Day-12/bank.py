"""
here create a bankaccount class for deposite
and withdraw function.
"""

# ---------------------------------------------

class BankAccount:
    """simple bank account class."""

    def __init__(self, balance: int = 0) -> int:
        self.balance = balance


    def deposit(self, amount: int) -> int:
        """Add money to account."""
        self.balance += amount
        return self.balance


    def withdraw(self, amount: int) -> int:
        """Withdraw money from account."""
        self.balance -= amount
        return self.balance    
