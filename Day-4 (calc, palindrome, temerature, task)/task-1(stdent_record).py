"""
  Here i performed a student record system, which has
  functionality like add, search, list and delete record.
"""
# ------------------------------------------------------------------


# Function of StudentRecord - add , search , list , delete

# Add records function


def student_record_add(student_detail_list: list) -> None:
    """
        It takes a name, rollno and marks from user, and 
        add in student_detail_list.

        Args :
            student_detail_list (list) : list containing all
                                        student record.

        Return :
            None

    """
    name = input("Enter your name : ")
    rollno = input("Enter your rollno (10 digits) : ")
    marks = input("Enter your marks : ")

    if (len(rollno)==10): # It add only if rollno 10 digit.
        student_detail_list.append({
                'name' : name, 
                'rollno' : rollno,
                'marks' : marks
        })
    else:
        print("Enrollment not match according 10 number length")


# List function


def student_list(student_detail_list: list) -> None:
    """
        It prints all info of Student_detail_list ,
        name , rollno and marks.

        Args :
            student_detail_list (list) : list all details

        Return :
            None    
    """

    print("Records are ------")

    for student in student_detail_list:
        # Print every data
        print(
            f"Name: {student['name']}, "
            f"Rollno: {student['rollno']}, "
            f"Marks: {student['marks']}"
        )  # Name: nigam, Rollno: 7458205132, Marks: 95


        """ print data dictionary form inside list"""
        # print(student_detail_list) 


# Search function


def student_search(student_detail_list: list) -> None:
    """
        It search for name and print it's info like
        name, rollno and marks

        Args :
            student_detail_list (list) : list for search student

        Return :
            dict : matched records.   
    """

    name = input("Enter name to search: ")

    print("Here all records are...")

    for student in student_detail_list:
        # Iterate all records and match record print
        if student['name'] == name:
            print(student_detail_list) 
            return    
        else:
            pass

    print("Name you search not found..")    


# Delete function


def student_delete(student_detail_list: list) -> None:
    """
        It delete record of student
        that user send name as input.

        Args : 
            student_detail_list (list) : list containing student

        Return : 
            None    
    """
    name = input("Enter name for delete record: ")

    for student in student_detail_list:
        #Iterates through all records and fetch matched record
        if student['name'] == name:
            student_detail_list.remove(student) # remove del record
            print("record deleted successfully..")
            return
        
    print("Recorded are deleted..")    


# ------------------------------------------------------------------

def main() -> None:
    """Main function to run program."""

    student_detail_list = []

    while True:
        print("\nStudent Record System..")
        print("press 0: Exit")
        print("press 1: Enter Records")
        print("press 2: List Records")
        print("press 3: Search Records")
        print("press 4: Delete Records")

        choice = int(input("Enter your Choice : "))

        if choice == 0:
            print("Exit....")
            break

        elif choice == 1:
            student_record_add( student_detail_list)

        elif choice == 2:
            student_list(student_detail_list)

        elif choice == 3:
            student_search(student_detail_list)    

        elif choice == 4:
            student_delete(student_detail_list)  

        else:
            print("Invalid Choice..")      

# ---------------------------------------------------------------

if __name__ == "__main__":
    main()   

