# ----comparision operator (==, !=, >,<,>=,<=) ---
num1 = 2
num2 = 4

print("num1 == b", num1 == num2)  # false
print(num1 != num2)  # true
print(num1 > num2)  # false
print(num1 < num2)  # true
print(num1 >= num2)  # false
print(num1 <= num2)  # true


#  ----logical operator (and,or,not)-----
print("true and false", True and False)  # false
print(True or False)  # true
print(not True)  # reverse of true , falsesss


# ---nested conditions---
age = 20
voter = False

if age >= 18:
    print("you are eligible for vote..")

    if voter:
        print("you can vote")
    else:
        print("you can't vote")

else:
    print("you are not eligible for vote")
