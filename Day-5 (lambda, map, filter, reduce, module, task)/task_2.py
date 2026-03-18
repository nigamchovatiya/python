# import statement

import math
import random
from datetime import datetime
import os

print("square root of 25:", math.sqrt(25)) # 5
print("pi value:", math.pi) # 3.14
print("Factorial Of 5:", math.factorial(5)) # 120

print(random.random()) # random number generate


print("today date:", datetime.today()) # 2026-03-05 17:30:15

print(os.getcwd()) # d:\python
print(os.listdir()) # ['Day-1', 'Day-2', 'Day-3'] 


# ------------------------------ Task ---------------------------------


# random password
n = 8

for i in range(n):
    print(f"{i} Random password 10 digit", random.randint(9999999, 99999999))  


# display current date

current_date = datetime.today()
print("Y-M-D:", current_date)


# list directory of files

current_directory = '.'
all_files = os.listdir(current_directory)

print(all_files)


