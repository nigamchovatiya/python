"""
  Here i performed 10 random password generate, display 
  formatted dates and list a file directory.
"""

# -----------------------------------------------------------------

import random
import string
import datetime
import os

# -----------------------------------------------------------------


# Function of user_sort 

def random_password(length: int) -> None:
    """
    This generate a 8 lenght random password

    Args:
        length(int) : Take a length of password   

    Return:
        None : print 10 random password   
    """

    print("10 randome password...")

    character = string.ascii_letters + string.digits + string.punctuation

    n = 10 # 10 random password

    for i in range(n):
        password = ""

        for j in range(length): # 8 length password
            password += random.choice(character) 

        print(f"password{i+1}:", password)    
        

# current_date

def current_date() -> None:
    """
    This generate a current date 

    Args:
        None

    Return:
        None        
    """

    print("Today date & time is...")

    now = datetime.datetime.now()
    print("current date&time:", now)

    print("D-M-Y:",now.strftime("%d-%m-%y"))
    print("weekday, date month year:",now.strftime("%A, %d %b %y"))
    print("hour minute second:",now.strftime("%H:%M:%S"))


# current_file_directory

def current_file_directory() -> None:
    """
    This print a current file structure 

    Args:
        None

    Return:
        None
    """

    print("current file directory...")


    current_directory = os.listdir()
    print(current_directory)
       

# -----------------------------------------------------------------

def main() -> None:
    """main function run the program"""

    random_password(8)

    current_date()

    current_file_directory()    
  

# ---------------------------------------------------------------

if __name__ == "__main__":
    main()



