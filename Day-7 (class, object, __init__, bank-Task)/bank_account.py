"""
  Simple BankAccount class example with deposit, withdraw and 
  getbalance methods.
"""


# ------------------------------------------------------------------- 

class BankAccount:
    """A Simple BankAccount class"""

    def __init__(self, currentbalance: int) -> None:
        """Intialize currentbalance."""
        self.currentbalance = currentbalance

    def deposit(self, deposit: int) -> str:
        """Add money to account."""
        self.currentbalance += deposit
        return f"{deposit} ammount deposit in your account."

    def withdraw(self, withdraw: int) -> str:
        """Withdraw money from account."""
        self.currentbalance -= withdraw
        return f"{withdraw} ammount withdrawn in your account."

    def get_balanace(self) -> str:
        """Total balance from account."""
        return f"{self.currentbalance} total balance in your account."
    
    def __str__(self) -> str:
        return "this is object representation."


user1 = BankAccount(100000)
user2 = BankAccount(50000)

print(user1) # this is object representation.

print("--------User1 BankAccount--------")
print(user1.get_balanace()) # 100000
print(user1.deposit(45000)) # +45000
print(user1.withdraw(40000)) # -40000
print(user1.get_balanace()) # 105000

print("\n--------User2 BankAccount-------")
print(user2.get_balanace()) # 50000
print(user2.deposit(20000)) # +20000
print(user2.withdraw(10000)) # -10000
print(user2.get_balanace()) # 60000
 
