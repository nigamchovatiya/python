"""
   here i perform a save data in contactlist.json
   and print json save data.
"""

# --------------------------------------------------

import json

# --------------------------------------------------

contact_list = [
    {"name": "rahul", "phone": 8574123690,
    "email": "rahul@gmail.com"},
    {"name": "mohan", "phone": 8745960213,
    "email": "mohan22@gmail.com"},
    {"name": "soham", "phone": 7459861232,
    "email": "soham45@gmail.com"}
]


# data save contactlist.json file

try: 
    with open('contactlist.json', 'w') as file:
        json.dump(contact_list, file, indent=4)

except Exception as e:
    print("Error saving contacts.", e) 


# --------------------------------------------------

# load save data 

try:
    with open('contactlist.json', 'r') as file:
        list_data = json.load(file)

    for data in list_data:
        print(data) # dictionary form data print.

except Exception as e:
    print("Error data reading.", e)
