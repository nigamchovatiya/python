"""
  Here i performed a basic temperature calculator in user given 
  temerature and return their according a result.
"""

# --------------------------------------------------------------

# Function of Temerature - celsius_to_fahrenheit, 
#                          fahrenheit_to_celsius

# celsius_to_fahrenheit

def celsius_to_fahrenheit(c: float) -> float:
    """
    This performs celsius to fahrenheits of given numbers and
    returns the fahrenheits.
 
    Args:
        c(float) : First temerature
 
    Return:
        float : Result after doing fahrenheit
    """
    
    return (c * 9/5) + 32


# fahrenheit_to_celsius

def fahrenheit_to_celsius(f: float) -> float:
    """
    This performs fahrenheit to celsius of given numbers and
    returns the celsius.
 
    Args:
        f(float) : First temerature
 
    Return:
        float : Result after doing celsius
    """
    
    return (f - 32) * 5/9


# --------------------------------------------------------------

def main() -> None:
    """main function run the program"""

    print("temerature Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")

    choice = input("Enter a choice (1-2) ")

    if choice == "1":
        temp = float(input("Enter temperature in Celsius: "))
        print("Fahrenheit:", celsius_to_fahrenheit(temp))

    elif choice == "2":
        temp = float(input("Enter temperature in Fahrenheit: "))
        print("Celsius:", fahrenheit_to_celsius(temp))

    else:
        print("Invalid Choice..")



# ---------------------------------------------------------------

if __name__ == "__main__":
    main()

