var_a = 25
var_b = 25.8
name = "john"
status = True

print(var_a)
print(type(var_b))
print(name)
print(type(status))


age = 21
id_status = False

if age > 18:
    print("you are eligible for a testdrive...")

    if id_status == True:
        print("You can testdrive.")

    else:
        print("You can't drive your status is false.")

else:
    print("you can't eligible.")


user_list = ['nigam', 1, True]
print(user_list[0])

user_list[2] = False
print(user_list)
print(user_list[::2])
print(user_list[1:])

user_detail = ('john', 21, 95)
print(user_detail)
# user_detail(0) == 'dor' # typeError 
print(user_detail[2])

marks = {1, 2, 3, 4, 5, 2, 3, 4, 5, 1}
marks2 = {4, 5, 6 ,8}
print(marks) # duplicate remove
print(marks | marks2) # union
print(marks & marks2) # intersetion
print(marks - marks2) # diffrence


user_info = {
    "student1": {
        "name": "john",
        "rollno": 21,
        "marks": 90
    },
    "student2": {
        "name": "doe",
        "rollno": 22,
        "marks": 92
    }
}

print(user_info["student1"]["name"]) # john
print(user_info["student2"]["marks"]) # 92


def addition(a, b):
    print("addition of two number is:", a + b)

addition(9, 10)    


def user_name(name = "Default"):
    print(f"hello! {name}, welcome to collage")

user_name("jay") # jay   
user_name() # default parameter   


n = 5
for i in range(n):
    for j in range(i+1):
        print("*",end=" ")

    print()   


# ------- reverse pattern ----------
print("----------reverse pattern-----")
n=5
for i in range(n):
    for j in range(n-i):
        print("*", end=" ")

    print()   


# ------- reverse hill pattern ----------
print("---------- reverse hill pattern---------")

n=5
for i in range(n):
    for j in range(i):
        print(" ",end=" ")
    for j in range(n-i):
        print("*", end=" ")

    for j in range(n-i-1):
        print("*", end=" ")
    for j in range(i):
        print(" ",end=" ")
                
    print()    


print("----------hill pattern---------")

n=5
for i in range(n):
    for j in range(n-i):
        print(" ", end=" ")
    for j in range(i+1):
        print("*", end=" ") 

    for j in range(i):
        print("*", end=" ") 
    for j in range(n):
        print(" ", end=" ")
       
    print()    


# gst price calculator
price_list = {"Tv": 25000, "Ac": 35800, "Phone": 25500, "Fridge": 65700} # dictionary of pricelist
tax = 0.18 # 18% Gst

gst_total_price = list(
    map(lambda val: val + (val * tax), price_list.values())
    )

# print("without Gst price:",price_list)
# print("18% Gst add after total price is:", gst_total_price)

print("Tv: 25000 after add 18% gst:", gst_total_price[0]) # 29500
print("Ac: 35800 after add 18% gst:", gst_total_price[1]) # 42244
print("Phone: 25500 after add 18% gst:", gst_total_price[2]) # 30090
print("Fridge: 65700 after add 18% gst:", gst_total_price[3]) # 77526