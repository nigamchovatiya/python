"""
  csv file read operation 
  with read csv, write and read csv as dictionary.
"""
# read data in file.csv

import csv

try:
    
    with open('file.csv', 'r') as file:
        read = csv.reader(file)

        for data in read:
            print(data)

except FileNotFoundError:
    print("Error: file not found.")            


"""csv file write operation"""
# data write in data.csv file 

data = [
    ["id", "name", "age"],
    [1, "John", 25],
    [2, "Doe", 28],
    [3, "Samir", 35]
]

try:

    with open('data.csv', 'w', newline="") as file:
        writer = csv.writer(file)
        writer.writerows(data)

except PermissionError:
    print("Error: permission denied.")



"""csv dictionary reader"""    
# data give in dictionary

try:
    
    with open('data.csv', 'r') as file:
        read = csv.DictReader(file)

        for row in read:
            print(row) # print key valu pair data

except FileNotFoundError:
    print("Error: file not found.")            