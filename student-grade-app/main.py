"""
  here i create a main.py in that
  all function and file call here.
  manage.py after create main.py
  handle entry point.
"""

# ----------------------------------------

from manager import StudentManager

# ----------------------------------------


def main() -> None:
    """main function run the program"""

    # create StudentManager class object
    manager = StudentManager() 

    while True:
        print("\n------- Student grade manager -------")
        print("1. Add student")
        print("2. List student")
        print("3. Search student")
        print("4. Delete student")
        print("5. Exit")

        try:
            choice = int(input("Enter a choice: "))
            
        except ValueError:
            print("Invalid input! Enter number only.")
            continue

        if choice == 1:
            
            try:
                student_id = int(input("Enter student id: "))

            except ValueError:
                print("Invalid ID!")
                continue
            
            student_name = input("Enter a student name: ")
            student_section = input("Enter a student section: ")
            
            subject = {}

            try:
                n = int(input("Enter number of subjects: "))

                if n <= 0:
                    print("Invalid number of subjects!")
                    continue

            except ValueError:
                print("Enter valid number!")
                continue

            for _ in range(n):

                while True:
                    sub = input("Enter subject name: ")

                    if not sub:
                        print("Subject name cannot be empty!")
                        continue

                    try:
                        marks = int(input("Enter marks for subject: "))

                        if 0 <= marks <= 100:
                            subject[sub] = marks
                            break   
                        else:
                            print("Marks must be between 0 and 100!")

                    except ValueError:
                            print("Please enter valid number for marks!")    


            # data add manager class add student function
            manager.addstudent(student_id, student_name,
                            student_section, subject)
            
            

        elif choice == 2:
            manager.liststudent()

        elif choice == 3:
            try:
                student_id = int(input("Enter a id for you want to search: "))
                manager.searchstudent(student_id)  
            except ValueError:
                print("invalid id!")          

        elif choice == 4:
            try:
                student_id = int(input("Enter a id for you want to delete: "))
                manager.deletestudent(student_id)
            except ValueError:
                print("invalid id!")    

        elif choice == 5:
            print("Exited...")
            break

        else:
            print("Invalid choice..")


# -----------------------------------------

if __name__ == "__main__":
    main()