"""
Read a infodata.csv file, filter row by marks,
filtered result print new filterdata.csv file.
"""

# -------------------------------------------------------

import csv

# -------------------------------------------------------

filter_data = [] # empty list assign for filter data

try:
    """open csv file and read data"""

    with open('infodata.csv', 'r') as file:
        read = csv.DictReader(file) # read dictionary

        for data in read:
            if int(data["marks"]) > 75: # marks > 75
                filter_data.append(data)

except FileNotFoundError:
    print("Error: file not found.")

except ValueError:
    print("Error: marks value must be number.")   

finally:
    print("read operation completed..")     


# -------------------------------------------------------

try:
    """write filtered data new csv file"""

    with open('filterdata.csv', 'w', newline="") as file:
        # fieldnames for a new csv file print
        fieldnames = ["id", "name", "marks"]

        # write dictionary
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader() # write header
        writer.writerows(filter_data) # write filter row

except PermissionError:
    print("Error: not permission on writing file.")     

finally:
    print("write operation completed..")       


# -------------------------------------------------------

try:
    """open filerdata.csv and read data"""

    with open('filterdata.csv', 'r') as file:
        data_read = csv.DictReader(file)

        for data in data_read:
            print(data) # print filter data.

except FileNotFoundError:
    print("Error: file not found.")    

finally:
    print("read operation completed..")            

