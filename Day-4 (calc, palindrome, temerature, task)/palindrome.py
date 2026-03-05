"""
  Checks for the word whether it palingdrome or not.
"""

# --------------------------------------------------------------

# Function of palindrome - check_palindrome


def check_palindrome(word: str) -> None:
    """
    This performs word is palindrome or not.
 
    Args:
        word(str) : User input Word for check
 
    Return:
        None
    """

    if word == word[::-1]:
        print(f"Enter {word} is palindrome")

    else:
        print("Enter Word is not palindrome.")    
        

# --------------------------------------------------------------

def main() -> None:
    """main function run the program"""

    word = input("Enter the word: ")

    check_palindrome(word)



# ---------------------------------------------------------------

if __name__ == "__main__":
    main()
