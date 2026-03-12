"""
  here i create a custome exception,
  and catch all exception.
"""

# --------------- custome error exception ---------------

# custome error name
class InvalidNumberError(Exception):
    pass


try:
    num = int(input("Enter a positive number :"))

    if num < 0:
        raise InvalidNumberError("Error: enter a" \
                                " positive number.")
    
    else:
        num += 10
        print("num is:", num)

# exception handling.
except InvalidNumberError as e:
    print(e)

# except number value error handling.
except ValueError:
    print("Error: enter a valid number.")


# ----------------- catch all exception -------------------

try:
    x = int("abc")

except Exception as e:
    print("Error:", e)    
