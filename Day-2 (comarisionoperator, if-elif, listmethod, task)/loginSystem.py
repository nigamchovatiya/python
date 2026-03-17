
# ----------------------------------------------- simple login system ----

username = "nigam"  # hardcoded data
password = "1234"

uname = input("Enter a username: ")  # user input
pass1 = input("Enter a password: ")

if uname == username:
    print("Correct Username")  # username correct
    if password == pass1:
        print("Correct Password")
        print(f"Welcome {uname} in system")  # password also correct
    else:
        print("incorrect Password..")
else:
    print("Usename not matched..")  # username not match


# ---------------------------------------------------- Using Function ----

"""
Simple login authentication program.
"""


def authenticate_user(input_username: str, input_password: str) -> bool:
    """
    Validate user credentials.

    Args:
        input_username (str): Username entered by user.
        input_password (str): Password entered by user.

    Returns:
        bool: True if credentials are correct, otherwise False.
    """

    # Stored credentials
    stored_username = "nigam"
    stored_password = "nigam@123"

    # Check username
    if input_username != stored_username:
        print("Username not matched.")
        return False

    print("Correct username.")

    # Check password
    if input_password != stored_password:
        print("Incorrect password.")
        return False

    print("Correct password.")
    return True


def main():
    """
    Main function to handle user input and login process.
    """

    # Get user input
    username = input("Enter a username: ")
    password = input("Enter a password: ")

    # Authenticate user
    if authenticate_user(username, password):
        print(f"Welcome {username} to the system!")


# Run program
if __name__ == "__main__":
    main()
