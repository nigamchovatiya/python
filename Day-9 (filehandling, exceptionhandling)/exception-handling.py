""" try, except, finally, 
    mulitple exception type, raise,
    custome exception.
"""

# try..except ----------------

try:
    num = int(input("enter a number: "))
    result = 10 / num
    print(result)

except ZeroDivisionError:
    print("can't divide by zero.")

except ValueError:
    print("invalid input.")    


# try...except...else....finally ----------

try:
    num = int(input("enter a number: "))
    result = 10 / num

except ZeroDivisionError:
    print("can't divide by zero.")

except ValueError:
    print("invalid input.")  

else:
    print(result)

finally:
    print("program completed..")    


# multiple exception type ------

try:
    result = 10 / 0

except (ZeroDivisionError, ValueError):
    print("invalid input..")


# raise a mannually exception -----

age = 18

if age < 18:
    raise ValueError("age must be a 18 or above..")

print("get a license.")


# custome exception with try/except -------------

class InvalidInputError(Exception):
    pass

try:
    marks = int(input("Enter a marks:"))

    if marks < 0:
        raise InvalidInputError("invalid marks.")

    print("marks:", marks)    

except InvalidInputError as e:
    print(e)
    
