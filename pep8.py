"""
module_name.py
 
Short module description.
 
Longer description explaining what this file does.
"""
 
# ─────────────────────────────────────────────────────────────
# Standard library imports
import os
import sys
 
# Third-party imports
# import requests
 
# Local application imports
# from utils.helper import some_function
 
 
# ─────────────────────────────────────────────────────────────
# Constants (UPPER_CASE)
MAX_USERS = 100
DEFAULT_TIMEOUT = 30
 
 
# ─────────────────────────────────────────────────────────────
class User:
    """
    Represents a system user.
 
    Attributes:
        username (str): The username of the user.
        age (int): The age of the user.
    """
 
    def __init__(self, username: str, age: int) -> None:
        """Initialize user with username and age."""
        self.username = username
        self.age = age
 
    def is_adult(self) -> bool:
        """
        Check if the user is an adult.
 
        Returns:
            bool: True if age >= 18, else False.
        """
        return self.age >= 18
 
 
# ─────────────────────────────────────────────────────────────
def add_numbers(a: int, b: int) -> int:
    """
    Add two numbers.
 
    Args:
        a (int): First number
        b (int): Second number
 
    Returns:
        int: Sum of a and b
    """
    return a + b
 
 
def print_user_info(user: User) -> None:
    """
    Print formatted user information.
 
    Args:
        user (User): User object
    """
    print(f"Username: {user.username}")
    print(f"Age: {user.age}")
    print(f"Adult: {user.is_adult()}")
 
 
# ─────────────────────────────────────────────────────────────
def main() -> None:
    """Main function to run the program."""
    user = User("yash", 21)
 
    print_user_info(user)
 
    result = add_numbers(5, 7)
    print(f"Sum: {result}")
 
 
# ─────────────────────────────────────────────────────────────
if __name__ == "__main__":
    main()