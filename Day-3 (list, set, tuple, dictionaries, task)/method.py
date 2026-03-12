# ----------------get(), items(), keys() and values()--------------------

dict2 = {
    "name": "john",
    "age": 21,
    "marks": 90,
    "city": "NYC"
}

print(dict2.get("marks"))  # 90
# get fetch data safer method if not data return none instead of error

print(dict2.items())  # return key-value pair

print(dict2.keys())  # get key only
print(dict2.values())  # get value only


# --------------------dictionary comprenhensive-------------------
dict2 = [1, 2, 3, 4]

# dict3 = {x: x*x for x in dict2} # 1:1 , 2:4, 3:9 , 4:16
dict3 = {x: x for x in dict2}  # 1:1 , 2:2, 3:3 , 4:4
print(dict3)
