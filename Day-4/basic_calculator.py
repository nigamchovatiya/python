"""
    Here i performed a basic calculator in user given number
    and return their according a operations.
"""

# --------------------------------------------------------------

import math

# --------------------------------------------------------------

# Function of Calculator - add , sub, div, mul 
#                          modulo , power, sqrt

# Number Function

def numbers() -> int:
    """
    Enter two numbers for we want to perform
    arithematic operations
 
    """
 
    first_number = int(input("Enter first number: "))
    second_number = int(input("Enter second number: "))
 
    return first_number, second_number
 
# Addition Function 
 
def addition(first_number, second_number) -> int:
    """
    This performs addition of two numbers and returns the
    result
 
    Args:
        first_number(int) : First operand
        second_number(int) : Second operand
 
    Returns:
        Result after performing addition on both operands
    """
 
    result = first_number + second_number
 
    return result
 
# Subtraction Function 
 
def substraction(first_number, second_number) -> int:
    """
    This performs addition of two numbers and returns the
    result
 
    Args:
        first_number(int) : First operand
        second_number(int) : Second operand
 
    Returns:
        Result after performing addition on both operands
    """
 
    result = second_number - first_number
 
    return result
 
# Multiplication Function 
 
def multiplication(first_number, second_number) -> int:
    """
    This performs addition of two numbers and returns the
    result
 
    Args:
        first_number(int) : First operand
        second_number(int) : Second operand
 
    Returns:
        Result after performing addition on both operands
    """
 
    result = first_number * second_number
 
    return result
 
# Division Function 
 
def division(first_number, second_number) -> float:
    """
    This performs addition of two numbers and returns the
    result
 
    Args:
        first_number(int) : First operand
        second_number(int) : Second operand
 
    Returns:
        Result after performing addition on both operands
    """
 
    result = first_number / second_number
 
    return result
 
# Modulos Function 
 
def modulos(first_number, second_number) -> int:
    """
    This performs addition of two numbers and returns the
    result
 
    Args:
        first_number(int) : First operand
        second_number(int) : Second operand
 
    Returns:
        Result after performing addition on both operands
    """
 
    remainder = first_number % second_number
 
    return remainder
 
# Power Function 
 
def power(first_number, second_number) -> int:
    """
    This performs addition of two numbers and returns the
    result
 
    Args:
        first_number(int) : First operand
        second_number(int) : Second operand
 
    Returns:
        Result after performing addition on both operands
    """
 
    result = first_number ** second_number
 
    return result
 
# Squareroot Function 
 
def square_root(number: int) -> int:
    """
    This performs Square root of given numbers and returns the
    result
 
    Args:
        number(int) : First operand
 
    Returns:
        Result after doing square root of number
    """
 
    result = math.sqrt(number)
 
    return result


# --------------------------------------------------------------

def main() -> None:
    """
    Main function to run program.
    """

    first_number, second_number = numbers()
 
    while True:
        
        print("1.Addition")
        print("2.Substraction")
        print("3.Multiplication")
        print("4.Division")
        print("5.Modulos")
        print("6.Power")
        print("7.Square Root")
        print("8.Exit")

        choice = int(input("Enter your choice: "))
 
        if choice == 1:
            result = addition(first_number, second_number)
            print(result)
        elif choice == 2:
            result = substraction(second_number, first_number)
            print(result)
        elif choice == 3:
            result = multiplication(first_number, second_number)
            print(result)
        elif choice == 4:
            result = division(first_number, second_number)
            print(result)
        elif choice == 5:
            result = modulos(first_number, second_number)
            print(result)
        elif choice == 6:
            result = power(first_number, second_number)
            print(result)
        elif choice == 7:
            result = square_root(first_number)
            print(result)
        elif choice == 8:
            break
 
        else:
            print("Invalid choice") 

# --------------------------------------------------------------

if __name__ == "__main__":
    main()