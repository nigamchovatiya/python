# -----if/else/elif ---conditinal statements--- 

# age = 13

# if age>=18:
#     print("You can drive..")
# else:
#     print("you can't drive..") 

# ---- elif   it like else if------

# age = 15

# if age>=18:
#     print("you can go for solo trip..")
# elif age>=16:
#     print("you can go for school trip") 
# elif age>=14:
#     print("you can go for one day trip.")
# else:
#     print("not go for any trip..")  


# --- boolean values-----
# True = 1
# False = 0

# ----comparision operator (==, !=, >,<,>=,<=) ---
# num1 = 2
# num2 = 4
# print("num1==b",num1==num2) # false
# print(num1!=num2) # true
# print(num1>num2) # false
# print(num1<num2) # true
# print(num1>=num2) # false
# print(num1<=num2) # true

#  ----logical operator (and,or,not)-----
# print("true and false",True and False) # false
# print(True or False) # true
# print(not True) # reverse of true , falsesss

# ---nested conditions---
# age = 20
# voter = False

# if age>=18:
#     print("you are eligible for vote..")

#     if voter:
#         print("you can vote")
#     else:
#         print("you can't vote")
# else:
#     print("you are not eligible for vote")            

# ---Grade Calculator---
# marks = int(input("enter a marks: "))

# if marks>=95:
#     print("Grade A+")
# elif marks>=85:
#     print("Grade A")
# elif marks>=75:
#     print("Grade B")
# elif marks>=65:
#     print("Grade C")
# elif marks>=45:
#     print("Grade D")
# else:
#     print("Grade F")            


# ----for and while loop----
# for i in range(5):
#     print(i) # 0 1 2 3 4

# i = 0
# while i<=4:
#     print(i)
#     i += 1  # 0 1 2 3 4

# range(start,stop, step)
# range(5) 0 to 4
# range(1,3) 1 to 3
# range(1,8,2) 1,3,5,7

#enumerate() replace counter variable
# fruits = ['apple','banana','orange']
# for index,i in enumerate(fruits):  # easily print index and value
#     print(f"{index}, {i}") # 0,apple 1,banana 2,orange

# ----break and continue-----
# for i in range(5):
#     if i==3:
#         break    # stop execution
#     print(i) # 0 1 2

# for i in range(6):
#     if i==4:
#         continue # skip current iteration value
#     print(i) # 0 1 2 3 5

# ---nested loop----
# for i in range(2):
#     for j in range(3):
#         print(i,j) # 00 01 02 10 11 12    

# print("loop exit..")

# ---- star pattern-----

# print("\n\nPattern 1")
# n=5
# for i in range(i, n+1):
#     for j in range(i):
#         print("*", end="")
#     print()

# n=5
# for i in range(5,0,-1): #start 5, 0 stop and -1 decrement
#     for j in range(i):
#         print("*", end="")
#     print()   
 
# print("\n\nPattern 2")
# n = 5
# for i in range(1,n+1):
#     for j in range(1,n+1-i):
#         print(" ",end="")
#     for j in range(1,i+1):
#         print("*",end="")
#     print("")
 
# print("\n\nPattern 3")
# n=5
# for i in range(n,0,-1):
#     for j in range(1,i+1):
#         print("*",end="")
#     print("")
 
# print("\n\nPattern 4")
# n=5
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j," ",end="")
#     print("")
 
# print("\n\nPattern 5")
# n=5
# k=1
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(k," ",end="")
#         k=k+1
#     print("")

# ----- multiplication table of num-----

# for i in range(1,11):
#     for j in range(1,11):
#          print(f"{i} X {j} = {i*j}")

#     print(" ") 

# ----prime number----
# for i in range(2,51):
#     flag=1
#     for j in range(2,i):
#         if(i % j == 0):
#             flag=0
#             break
#     if flag == 1:
#         print(i) # 2 5 7 11 13 17 19 etc..

# ---login system----
# username = "nigam" #hardcoded data
# password = "1234"

# uname = input("Enter a username: ") #user input
# pass1 = input("Enter a password: ")

# if uname == username:
#     print("Correct Username") # username correct
#     if password == pass1:  
#         print("Correct Password")
#         print(f"Welcome {uname} in system") # password also correct
#     else:
#         print("incorrect Password..")
# else:
#     print("Usename not matched..") #username not match  

"""
Simple login authentication program.
"""

# def authenticate_user(input_username: str, input_password: str) -> bool:
#     """
#     Validate user credentials.

#     Args:
#         input_username (str): Username entered by user.
#         input_password (str): Password entered by user.

#     Returns:
#         bool: True if credentials are correct, otherwise False.
#     """

#     # Stored credentials 
#     stored_username = "nigam"
#     stored_password = "nigam@123"

#     # Check username
#     if input_username != stored_username:
#         print("Username not matched.")
#         return False

#     print("Correct username.")

#     # Check password
#     if input_password != stored_password:
#         print("Incorrect password.")
#         return False

#     print("Correct password.")
#     return True


# def main():
#     """
#     Main function to handle user input and login process.
#     """

#     # Get user input
#     username = input("Enter a username: ")
#     password = input("Enter a password: ")

#     # Authenticate user
#     if authenticate_user(username, password):
#         print(f"Welcome {username} to the system!")


# # Run program
# if __name__ == "__main__":
#     main()
       

# import random
 
# def game_random(attempts : int, a : int , b : int) -> None:
#     """
#          number guessing game with limited attempts
 
#          Args :
#                 attempts (int) : Total attempts for user
#                 a (int) : starting range for number to guess
#                 b (int) : Ending range for number to guess
       
#          Returns :
#                 None : it prints user is win or loose.
 
#     """
 
#     # n = random.randint(a,b) # random generate a number
#     n = 8 # mannual given number
 
#     while(attempts > 0):
#         user_number = int(input(f"\nGuess a Number Between {a} and {b} : "))
#         if(n == user_number):
#             print("You Won")
#             break
#         else:
#             attempts -= 1 # attempts = attempts - 1 
#             print("You guess was incorrect ! Try Again")
#             print(f"No. of attempts left - {attempts}")        
#             print(" \n " * attempts)
   
#     if attempts == 0:
#         print("Oops ! You Lose the Game")
 
# game_random(3,1,10)
 

# ---- List -----
# create list
create_list = ["nigam", 1,True,4.5]
print(create_list) # nigam,1,True,4.5

create_list[2] = "string" # add a 2 index string

#index access
print(create_list[3]) #4.5

#append 
create_list.append(5)
print(create_list) # add 5 in list last position 

#pop
create_list.pop()
print(create_list) # delete last element of list 5

#remove
create_list.remove(1)
print(create_list) # remove a perticular element 1

#del
del create_list[0]
print(create_list) # delete element with index value

#sort
sort_list = [34 , 4 , 5 , 2 ,1]
sort_list.sort()
print(sort_list) # [1,2,4,5,34]

#slice
new_list = ['nigam', 21, 12, 'True', 'False']
# old_list = new_list[1:4]
print(new_list[1:4]) # 21,12,true
print(new_list[::2]) # nigam,12,false

#list comprehensive
new_list = [1,2,3,4,7,8]
even = [num for num in new_list if num % 2 == 0]
print(even) # filter even number with list comprehensive

odd = [num for num in new_list if num % 2 != 0]
print(odd) 


#new list
num = [1,3,5,7]
square = [x * x for x in num]
print(square) # 1,9,25,49

#find max
num = [1,56,78,9,60]
# num.sort()
largest = 0
for x in num:
    if largest < x:
        largest = x
print(largest) #78        

l1 = [2,45,1,3,4]
l1.sort()
print(l1[-1]) # 45

# top 3 student highest marks
high_marks = [51,56,85,74,95,76,96]
high_marks.sort()
# print( "first highest",high_marks[-1], "second highest ", high_marks[-2], "third highest" ,high_marks[-3])
descmarks = (high_marks[-1],high_marks[-2],high_marks[-3])
print(descmarks)

# third highest mark
marks = [76,98,85,70,96,99]
first = marks[0]
second = marks[1]
third = marks[2]

for mark in marks:
    if mark > first:
        third = second
        second = first
        first = mark

    elif mark > second:
        second = mark
    elif mark > third:
        third = mark

print("first: ", first) #99
print("second: ", second) #98
print("third: ", third) #96

    
          
