# import reduce
from functools import reduce


# Lambda function 
# anonymous function - (function withou name)

num_add = lambda a, b: a + b
print(num_add(2,3))  # 5

num_square = lambda x: x * x
print(num_square(4)) # 16


# map()
# apply function every element in list

number = [1, 2, 3, 4]
square = list(map(lambda x: x * x, number))
print(square) # [1,4,9,16]


# filter()
# select element based on condition

numbers = [1, 3, 2, 4, 6, 15, 22, 26]
even = list(filter(lambda x: x % 2 == 0, numbers))
print(even) # [2,4,6,22,26]


# sorted()
# sort element in ascending & descending

num = [22 ,12 ,4 ,5 ,1]
asce_num = sorted(num)
print(asce_num) # [1,4,5,12,22] Asce

desc_num = sorted(num, reverse=True)
print(desc_num) # [22,12,5,4,1] Desc


# reduce()
# combine all element in one value

sum = [1,2,4,6]
all_sum = reduce(lambda a, b: a + b, sum)
print(all_sum) # 13


# --------------------- sort list of dict by value ----------------------

user_list = [
    {"name": "nigam", "age": 20},
    {"name": "aman", "age": 18},
    {"name": "dev", "age": 22},
    {"name": "harikrushna", "age": 19},
]

sorted_details = sorted(user_list, key=lambda x: x["age"])
print(sorted_details) # Age sort ascending


# filter name with start specific name

user_list = [
    {"id": 1, "name": "Nigam"},
    {"id": 3, "name": "Devam"},
    {"id": 2, "name": "Dev"},
    {"id": 4, "name": "Harikrushna"},
    {"id": 10, "name": "Devarsh"},
    {"id": 11, "name": "Dhanush"},
]

filter_user = list(filter(lambda x: x['name'].startswith("D"), user_list))
print(filter_user) # Return name start with d


# Take input from a user to add a user_list

# user_input = []
# n = int(input("enter a which no.of user you enter. "))

# for i in range(n):
#     id = input("enter a id:")
#     name = input("enter a name:")

#     user_input.append({"id": id, "name": name})


# filter_user = list(filter(lambda x: x['name'].startswith("D"), user_input))
# print(filter_user) 

