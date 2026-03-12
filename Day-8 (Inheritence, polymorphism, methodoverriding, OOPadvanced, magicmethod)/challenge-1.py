"""
  Simple example savingsaccount add monthly
  interest rate.
"""


#------------------------------------------------------------

class BankAccount:
    """Parent BankAccount class."""

    def __init__(self, balance: float) -> float:
        self.balance = balance

    def get_balance(self) -> str:
        """Return current balance."""
        return f"{self.balance} is the current balance."
    
    # direct object print helpful.
    def __str__(self) -> str:
        """String representation of object."""
        return f"This is bank account class."


class SavingsAccount(BankAccount):
    """Child SavingsAccount class."""

    def monthlyInterest(self, interest: float) -> str:
        """Add monthly interest to the balance."""
        # Formula interest count
        interest_ammount = self.balance * (interest / 100)
        self.balance += interest_ammount
        return f"monthly interest {interest_ammount} " \
                "Rs. add in your current balance."            
   

user1 = SavingsAccount(75000)
user2 = SavingsAccount(9000)
user3 = SavingsAccount(4100)

print(user1) # this is bank account class.

print("---------User1----------")
print(user1.get_balance()) # 75000
print(user1.monthlyInterest(0.3)) # 225.0
print(user1.get_balance()) # 75225.0

print("\n---------User2----------")
print(user2.get_balance()) # 9000
print(user2.monthlyInterest(0.25)) # 22.5
print(user2.get_balance()) # 9022.5

