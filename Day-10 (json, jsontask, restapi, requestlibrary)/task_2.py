"""
  here i perform a python dictionary save
  json file and load data and verify data.
"""


# --------------------------------------------

import json

# --------------------------------------------

# python dictionary.
user_list = {
    "name": "user1",
    "userid": 12,
    "contact": 9874561230,
    "skill": ['cricket', 'hockey']
}

# convert dic obj into Json string
data = json.dumps(user_list)
print(data)

# data save list.json file
try:
    with open('list.json', 'w') as file:
        json.dump(user_list, file, indent=4)

    print(f"data successfully saved in list.json.")

except Exception as e:
    print("Error in writting file:", e)        


# ---------------------------------------------

# load save data
try:
    with open('list.json', 'r') as file:
        list_data = json.load(file)

    print("data loaded from file:", list_data)    

except Exception as e:
    print("Error in reading file:", e)            


# ----------------------------------------------

# verify data
if user_list == list_data:
    print("Data matched..")
else:
    print("Data not matched..")
