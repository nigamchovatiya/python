"""
  Here i perform cli calculator with basic functionality like
  add, sub, mul, div, mod, power, sqrt.
  
"""

# -----------------------------------------------------------------

import math

# -----------------------------------------------------------------


# addition

def add(num1: float, num2: float) -> float:
    """
    This performs addition of two numbers and returns the
    result
 
    Args:
        first_number(float) : First operand
        second_number(float) : Second operand
 
    Returns:
        Float : Result after performing addition
    """

    return num1 + num2  


# subtraction

def subtract(num1: float, num2: float) -> float:
    """
    This performs subtraction of two numbers and returns the
    result
 
    Args:
        first_number(float) : First operand
        second_number(float) : Second operand
 
    Returns:
        Float : Result after performing subtraction
    """

    return num1 - num2


# multiplication

def multiply(num1: float, num2: float) -> float:
    """
    This performs subtraction of two numbers and returns the
    result
 
    Args:
        first_number(float) : First operand
        second_number(float) : Second operand
 
    Returns:
        Float : Result after performing multiplication
    """

    return num1 * num2


# divisions

def divide(num1: float, num2: float) -> float:
    """
    This performs division of two numbers and returns the
    result
 
    Args:
        first_number(float) : First operand
        second_number(float) : Second operand
 
    Returns:
        Float : Result after performing division
    """

    if num1 and num2 >= 1:
        return num1 / num2
    
    else:
        print("num is not zero allowed.")    
        return None


# modulo

def modulo(num1: float, num2: float) -> float:
    """
    This performs modulo of two numbers and returns the
    result
 
    Args:
        first_number(float) : First operand
        second_number(float) : Second operand
 
    Returns:
        Float : Result after performing modulo
    """

    if num1 and num2 >= 1:
        return num1 % num2

    else:
        print("num is not zero allowed.")        
        return None


# power

def power(num1: float, num2: float) -> float:
    """
    This performs power of number and returns the
    result
 
    Args:
        first_number(float) : First operand
        second_number(float) : Second operand for power
 
    Returns:
        Float : Result after performing power
    """

    if num1 and num2 > 0:
        return num1 ** num2
        # return math.pow(num1,num2)
    
    else:
        print("num is not zero allowed..")
        return None


# square root

def sqrt(num1: float) -> float:
    """
    This performs squareroot of numbers and
    returns the result
 
    Args:
        first_number(float) : First operand
 
    Returns:
        Float : Result after performing squareroot
    """

    if num1 >= 1:
        return math.sqrt(num1)
    else:
        print("not allowed 0..")    
        return None


# -----------------------------------------------------------------

def history(history_cal: list) -> None:
    """
    Store and print calculator history.

    Args:
        history_cal (list): List storing history

    Return:
        None    
    """

    print("-------History------")
    
    # last 10 record print.
    for items in history_cal[-10:]:
        print(items)


# -----------------------------------------------------------------

def print_choice() -> None:
    """
    This performs print user choice
 
    Args:
        None 
 
    Returns:
        Float : Print choice selection every time 
    """

    print("\n----------CLI Calculator-------------")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulos")
    print("6. Power")
    print("7. Square root")
    print("8. History")
    print("9. Exit")


# -----------------------------------------------------------------


def main() -> None:
    """main function run the program"""

    history_cal = [] # empty list


    while True:

        print_choice() # Function call choice selection print.

        print("\n------------User choice--------------")

        choice = int(
            input("Enter a choice between (1-8): "
                  "select a choice according your need.\n")
        )


        if choice == 1:
            print("----------Addition------------")
            num1 = float(input("Enter a first number.\n"))
            num2 = float(input("Enter a second number.\n"))

            result = add(num1, num2)
            record = f"{num1} + {num2} = {result}"
            print("Addition:", record)

            history_cal.append(record) # add records


        elif choice == 2:
            print("----------Subtraction------------")
            num1 = float(input("Enter a first number.\n"))
            num2 = float(input("Enter a second number.\n"))

            result = subtract(num1, num2)
            record = f"{num1} - {num2} = {result}"
            print("Subtraction:", record)

            history_cal.append(record)


        elif choice == 3:
            print("----------Multiplication------------")
            num1 = float(input("Enter a first number.\n"))
            num2 = float(input("Enter a second number.\n"))

            result = multiply(num1, num2)
            record = f"{num1} * {num2} = {result}"
            print("Multiplication:", record)

            history_cal.append(record)

    
        elif choice == 4:
            print("----------Division------------")
            num1 = float(input("Enter a first number.\n"))
            num2 = float(input("Enter a second number.\n"))

            result = divide(num1, num2)
            record = f"{num1} / {num2} = {result}"
            print("Division:", record)

            history_cal.append(record)


        elif choice == 5:
            print("----------Modulo------------")
            num1 = float(input("Enter a first number.\n"))
            num2 = float(input("Enter a second number.\n"))

            result = modulo(num1, num2)
            record = f"{num1} % {num2} = {result}"
            print("Modulo:", record)

            history_cal.append(record)


        elif choice == 6:
            print("----------Power------------")
            num1 = float(input("Enter a first number.\n"))
            num2 = float(input("Enter a second number.\n"))

            result = power(num1, num2)
            record = f"{num1} ^ {num2} = {result}"
            print("Power:", record)

            history_cal.append(record)


        elif choice == 7:
            print("----------Square root------------")
            num1 = float(input("Enter a first number.\n"))

            result = sqrt(num1)
            record = f"SQRT of {num1} = {result}"
            print("Squareroot:", record)

            history_cal.append(record)


        # history print
        elif choice == 8:
            history(history_cal)  
               
            
        else:
            print("Exit...")
            break           
        

# ------------------------------------------------------------------

if __name__ == "__main__":
    main()

