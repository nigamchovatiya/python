# function creation. -----------
def user_student(): 
    print("student function..")

user_student() # calling function


# parameter and argument --------------

# normal parameter ---
def add_sum(a, b):
    return a + b

print(add_sum(2, 5)) # 7

# default parameter ---
def student(name = "John"): # pass parameter
    return f"hello {name}"

# pass argument
print(student("Doe")) # hello Doe 
print(student()) # hello John


# *args ----------------------
def sum(*args):
    print(args)

sum([1, 2, 5]) # [1, 2, 5]    


# **kwargs --------------------
def student_info(**kwargs):
    print(kwargs)

student_info(name = "john", age = 20, city = "NYC") # {'name': 'john', 'age': 20, 'city': 'NYC'}  


# local and global variable

marks = 90 # global variable

def student():
    
    marks = 95 # local variable
    print("local marks:", marks)


print("global marks:", marks) # 90
student() # 95