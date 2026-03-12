"""
  here i create a custome exception of Invalid age
  , email and use it in registration function.
"""


# ----------------------------------------------------

# create a custome InvalidAgeError exception class
class InvalidAgeError(Exception):
    pass

# create a cutome InvalidEmailError exception class
class InvalidEmailError(Exception):
    pass


# ----------------------------------------------------

def registration_form(firstname: str, lastname: str,
                    age: int, email: str) -> None:
    
    """
    This perform check age and print a firstname,
    lastname and age.

    Args:
        firstname(str) : Take a firstname of user input.
        lastname(str) : Take a lastname of user input. 
        age(int) : Take a age of user input.
        email(str) : Take a email of user input.  

    Return:
        None : Data print.  
    """


    # Age validation.
    if age < 0 or age > 110:
        raise InvalidAgeError("Error: Invalid age" \
                            ", Enter a valid age.")
    
    # Email validation.
    if "@gmail.com" not in email:
        raise InvalidEmailError("Error: Invalid Email" \
                        ", Enter a right Email formate.")
        
    else:
        print("firstname:", firstname)
        print("lastname:", lastname)
        print("age:", age)
        print("email:", email)
    

# ------------------------------------------------------

def main() -> None:
    """main function to run program."""

    try:

        firstname = input("Enter a first name. \n")
        lastname = input("Enter a last name. \n")
        age = int(input("Enter a age. \n"))
        email = input("Enter a Email address. \n")
    
        registration_form(firstname, lastname, age, email)


    except InvalidAgeError as e:
        # call class InvalidAgeError and Error msg print.
        print(e) 

    except InvalidEmailError as e:
        # call class InvalidEmailError and Error msg print.
        print(e)    

    except ValueError:
        print("Age must be number.")  


# ------------------------------------------------------

if __name__ == "__main__":
    main()