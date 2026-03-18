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
        print("5. Top Performer student list")
        print("6. Exit")

        try:
            choice = int(input("Enter a choice: "))
            
        except ValueError:
            print("Invalid input! Enter number only.")
            continue


        if choice == 1:
            
            try:
                student_id = int(input("Enter student id: "))

                if student_id <= 0:
                    print("Student ID must be positive!")
                    continue

                if len(str(student_id)) > 10:
                    print("Invalid id length enter 10 max number.")
                    continue

                if any(s.student_id == student_id for s in manager.students):
                    print("Id already Exist.")
                    continue
                 
            except ValueError:
                print("Invalid ID! enter only number")
                continue
            
            # name validation
            student_name = input("Enter a student name: ").strip()
            if not student_name:
                print("Name can't empty.")
                continue

            if 2 <= len(student_name) >= 15:
                print("Name must be atleast 2 characters.")
                continue
 
            # section validation        
            student_section = input("Enter a student standard: ").strip()

            if not student_section:
                print("Student section can't empty.")
                continue
            if len(student_section) < 2:
                print("Name must be at least 2 character.")
                continue
            
            subject = {}


            # subject count validation
            try:
                n = int(input("Enter number of subjects: "))

                if n <= 0 or n > 10:
                    print("Invalid number of subjects!")
                    continue

            except ValueError:
                print("Enter valid number!")
                continue


            # subject name validation    
            for _ in range(n):

                while True:
                    
                    sub = input("Enter subject name: ").strip().lower()  
                    
                    is_duplicate = False
                    for key in subject:
                        if sub[:3] == key[:3]:
                            print(f"{sub} duplicate not allowed.")
                            is_duplicate = True
                            break
                            

                    if not sub:
                        print("Subject name cannot be empty!")
                        continue

                    if len(sub) <= 2:
                        print("Subject name atleast 3 character.")
                        continue

                    
                    if is_duplicate == False:        
                        # marks validation    
                        try:
                            marks = int(input(f"Enter marks for {sub}: "))

                            if 0 <= marks <= 100:
                                subject[sub] = marks
                                break
                            else:
                                print("Marks must be between 0 and 100!")

                        except ValueError:
                                print("Please enter valid number for marks!")    


            # data add manager class add student function
            manager.addstudent(student_id, student_name.title(),
                            student_section.title(), subject)
            
            
        elif choice == 2:

            if not manager.students:
                print("No record are in list please add a record first.")

            else:
                manager.liststudent()


        elif choice == 3:
            try:
                student_id = int(input("Enter Student ID to search: "))
                manager.searchstudent(student_id)  
            except ValueError:
                print("Invalid id!")          


        elif choice == 4:
            try:
                student_id = int(input("Enter a id for you want to delete: "))
                manager.deletestudent(student_id)
            except ValueError:
                print("Invalid id!")    


        elif choice == 5:

            if not manager.students:
                print("Empty records please add a records list.")

            else:    
                print("Top performer (GPA > 3.5) ------")
                manager.top_performer()


        elif choice == 6:
            print("Exited...")
            break


        else:
            print("Invalid choice..")


# -----------------------------------------

if __name__ == "__main__":
    main()