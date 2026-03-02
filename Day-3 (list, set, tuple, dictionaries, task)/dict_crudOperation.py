#------------- dictionaries ------------
# create
dict1 = {
    "name": "nigam",
    "age": 21,
    "course": "python"
}
print(dict1)

# read
print(dict1["name"])
print(dict1["course"])
print(dict1.get("age"))
print(dict1["city"])  # error
print(dict1.get("city"))  # return none

# update
dict1['age'] = 22  # update
dict1['name'] = "John"  # update
dict1['city'] = "NYC"  # add new key value
print(dict1)

# delete
dict1.pop("age")  # pop using delete
del dict1["city"]  # del using
print("age & city removed :", dict1)

# nested dictionary
student = {
    "student1": {
        "name": "john",
        "marks": 95
    },
    "student2": {
        "name": "virat",
        "marks": 98
    }
}

print(student["student1"]["name"])  # john
print(student["student2"]["marks"])  # 98
