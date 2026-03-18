"""
  Here i performed a csv data split and,
  print into a lists
"""

# -------------------------------------------------------------


# Function of data_csv perform split,strip and print list


def data_csv(student_data: list) -> None:
    """
        It takes hard cord csvdata and split
        in the list.

        Args:
            student_data (list): list data

        Return:
            None   
    """

    csv_data = """ id,name,age,city
    1,nigam,20,ahmedabad
    2,yash,21,surat
    3,kevin,22,bhuj
    4,krish,25,vadodara
    """

    #csv data clean and split
    datacsv = csv_data.strip().split("\n") 

    keys = datacsv[0].strip().split(",") # key 0 index
    values = datacsv[1:] # 1 to n value
    
    # print(keys)
    # print(values)

    
    # Iterate through all values and append key and value. 
    for value in values:
        val = value.split(",")
        val[0] = val[0].strip()
        student_data.append({
            keys[0]:val[0],
            keys[1]:val[1],
            keys[2]:val[2],
            keys[3]:val[3],
        })

    print(student_data)    

# -------------------------------------------------------------

def main() -> None:
    """Main function to run program."""

    student_data = []
    
    data_csv(student_data)


# -------------------------------------------------------------

if __name__ == "__main__":
    main() 

