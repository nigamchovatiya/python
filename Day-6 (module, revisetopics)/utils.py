"""
  Here i create a 5 reusable function and call in main.py
"""

# ---------------------------------------------------------------

# 1 function

def add(num1: int, num2: int) -> int:
    """
    This perform add operation and print sum

    Args:
        num1(int) : Take a user input during function call   
        num2(int) : Take a user input during function call   

    Return:
        int : Return sum of two number   
    """

    totalsum = num1 + num2
    return totalsum


# 2 function

def sub(num1: int, num2: int) -> int:
    """
    This perform sub operation and print sub

    Args:
        num1(int) : Take a user input during function call   
        num2(int) : Take a user input during function call   

    Return:
        int : Return sub of two number   
    """

    
    sub = num1 - num2
    return sub


# 3 function

def user_details(name: str, surname: str) -> str:
    """
    This perform name and string get and print.

    Args:
        name(str) : Take a name input during function call   
        surname(str) : Take a surname input during function call   

    Return:
        str : Return string of name, surname   
    """

    return name, surname


# 4 function

def verify(age: int) -> str:
    """
    This perform if-elif condition and give a according result.

    Args:
        age(int) : Take age input during function call  

    Return:
        str : Return matched condition   
    """

    if age < 18:
        return "you can't get apply for licence."       

    elif age >= 18:
        return "you can apply for licence."

    else:
        return "you can't age is in minus"


# 5 function

def verify_usercity(city: str) -> str:
    """
    This perform if-elif condition and give a according result.

    Args:
        city(str) : Take city input during function call  

    Return:
        str : Return matched condition    
    """

    if city == "ahmedabad":
        return "you can live in ahmedabad"

    elif city == "surat":
        return "you can live in surat."
  
    elif city == "vadodara":
        return "you can live in vadodara."

    else:
        return "you are out of town."  
      