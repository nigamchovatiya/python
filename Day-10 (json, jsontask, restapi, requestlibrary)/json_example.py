import json


"""------ json.dumps() ---------""" 
"""convert python - json string"""

# data = {"name": "john", "age": 26, "skill": ['read', 'write']}

# json_string = json.dumps(data)
# print(json_string)


"""------ jason.loads() -------"""
"""convert json string - python object"""

# json_string = '{"name": "Jonh", "age": 23}'

# data = json.loads(json_string)
# print(data)
# print(type(data))


"""--------- json.dump() ------- """
"""write python object - json file"""

# data = {"name": "john", "age": 25, "skill": ['read', 'write']}

# with open('data.json', 'w') as file:
#     json.dump(data, file)


"""--------- json.load() ------- """
"""read json file -  python object """

# with open('data.json', 'r') as file:
#     data = json.load(file)

# print(data)   


"""------ pretty printing json ---------""" 
"""it use better redablity."""

# data = {"name": "john", "age": 26, "skill": ['read', 'write']}

# json_string = json.dumps(data, indent=4)
# print(json_string)


"""--------- nested data -------"""
data = {
    "name": "john",
    "age": 23,
    "education": {
        "degree": "MCA",
        "year": 4
    },
    "skill": ['read', 'write']
}


json.dumps(data, indent=4)
# access nested data
print(data["education"]["degree"])