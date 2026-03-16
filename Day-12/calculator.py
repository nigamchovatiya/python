"""
here create a 5 function of calculator
"""

# -------------------------------------------

def add(num1: int, num2: int) -> int:
    """Return the sum of two numbers."""
    return num1 + num2


def subtract(num1: int, num2: int) -> int:
    """Return the difference of two numbers."""
    return num1 - num2


def multiply(num1: int, num2: int) -> int:
    """Return the product of two numbers."""
    return num1 * num2


def divide(num1: int, num2: int) -> float:
    """Return the division of two numbers."""
    if num2 == 0:
        raise ValueError("Cannot divide by zero")
    return num1 / num2


def modulo(num1: int, num2: int) -> int:
    """Return the remainder of two numbers."""
    return num1 % num2