"""
  Here i performed sort of dictionary value and 
  filter names with specfic letter.
  
"""

# --------------------------------------------------------------

# Function of user_sort 


def user_sort(user_list: list) -> None:
    """
    This perform sort operation on userlist and return 
    age sorted data

    Args:
        user_list(list) : Take a hardcorded user list   

    Return:
        None : Sorted data print   
    """

    sorted_details = sorted(user_list, key=lambda x: x["age"])
    
    # Sorted data by age print
    print("Sorted by age:", sorted_details)    
     

# user_filter

def user_filter(user_data: list) -> None:
    """
    This perform filter operation on userdata and return 
    specific name data.

    Args:
        user_data(list) : Take a hardcorded user list   

    Return:
        None : Filtered data print   
    """

    filter_user = list(
        filter(
            lambda x: x['name'].lower().startswith("d"), user_data
        )
    )

    # Filter data and D start name print
    print("Filter with 'D' name:", filter_user) 
       

# -----------------------------------------------------------------

def main() -> None:
    """main function run the program"""

    user_list = [
        {"name": "nigam", "age": 20},
        {"name": "aman", "age": 18},
        {"name": "dev", "age": 22},
        {"name": "harikrushna", "age": 19}
    ]

    user_sort(user_list) # Function call with argument

    user_data = [
        {"id": 1, "name": "Nigam"},
        {"id": 3, "name": "Aman"},
        {"id": 2, "name": "Dev"},
        {"id": 4, "name": "Harikrushna"},
        {"id": 10, "name": "Devarsh"},
        {"id": 11, "name": "Dhanush"}
    ]

    user_filter(user_data) 
  

# ---------------------------------------------------------------

if __name__ == "__main__":
    main()



