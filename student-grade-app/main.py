"""
  here i create a main.py in that
  all function and file call here.
  manage.py after create main.py
  handle entry point.
"""

# ----------------------------------------

from manager import StudentManager
import re

# ----------------------------------------


def main() -> None:
    """Run the Student Grade Manager program."""

    manager = StudentManager()
    manager.load_json()

    while True:
        print("\n------- Student Grade Manager -------")
        print("1. Add students")
        print("2. List students")
        print("3. Search students")
        print("4. Update students")
        print("5. Delete students")
        print("6. Top performer students list")
        print("7. Exit")

        # Menu choice
        try:
            choice = int(input("Enter a choice: "))
        except ValueError:
            print("Invalid input! Enter a number only.")
            continue

        
        if choice == 1:

            # Student ID 
            while True:
                try:
                    student_id = int(input("Enter student ID: "))
                except ValueError:
                    print("Invalid ID! Enter numbers only.")
                    continue

                # check id is not negative
                if student_id <= 0:
                    print("Student ID must be a positive number.")
                    continue

                # check id len is 10    
                if len(str(student_id)) > 10:
                    print("Student ID too long — maximum 10 digits.")
                    continue

                # check student id exist students[] list    
                if any(s.student_id == student_id for s in manager.students):
                    print(f"ID {student_id} already exists. Use a different ID.")
                    continue

                break 


            # Student Name 
            name_pattern = r"^[A-Za-z]{2,}(?: [A-Za-z]+)*$"

            while True:
                student_name = input("Enter student name: ").strip()

                # check name empty 
                if not student_name:
                    print("Name cannot be empty.")
                    continue

                # check name only letter contains    
                if not re.fullmatch(name_pattern, student_name):
                    print("Invalid name — letters only")
                    continue

                # check name len >! 50    
                if len(student_name) > 50:
                    print("Name too long.")
                    continue

                break   


            # Student Section 
            while True:
                student_section = input("Enter student section (e.g. 10A): "
                                "").strip()

                # section can't be empty
                if not student_section:
                    print("Section cannot be empty.")
                    continue

                # check section according to standard    
                if not re.fullmatch(r"[0-9]{2}\s*[A-Za-z]", student_section):
                    print("Invalid section(e.g. 10A, 11B).")
                    continue

                break 


            # Number of Subjects 
            while True:
                try:
                    n = int(input("Enter number of subjects (1–10): "))
                except ValueError:
                    print("Invalid input — enter a number.")
                    continue

                # check number of subject between 1 to 10    
                if n <= 0 or n > 10:
                    print("Number of subjects must be between 1 and 10.")
                    continue

                break  


            # Subject Names & Marks
            subject = {}

            sub_pattern = r"^[a-z]{3,}(?: [a-z]{2,})*$"

            for i in range(1, n + 1):
                print(f"Subject {i} of {n}")

                # -- Subject name --
                while True:
                    sub = input("Enter subject name: ").strip().lower()

                    # check sub can't empty
                    if not sub:
                        print("Subject name cannot be empty.")
                        continue

                    # check sub len atleast 3 char
                    if len(sub) < 3:
                        print("Subject name must be at least 3 characters.")
                        continue

                    # check subject name only letter    
                    if not re.fullmatch(sub_pattern, sub):
                        print("Subject name must contain letters only ")
                        continue

                    # check sub not exist in subjects[] list
                    if sub in subject:
                        print(f"'{sub}' already added. Enter a different subject.")
                        continue

                    # compare sub 3 char and key 3 for duplicate    
                    is_duplicate = False
                    for key in subject:
                        if sub[:3] == key[:3]:
                            print(f"{sub}' is too similar to ",
                                f"{key}' (duplicate not allowed).")
                            is_duplicate = True
                            break

                    if is_duplicate:
                        continue

                    break  

                # -- Marks --
                while True:
                    try:
                        marks = int(input(f"Enter marks for '{sub}' (0–100): "))
                    except ValueError:
                        print("Invalid input — enter a number.")
                        continue

                    # check marks between 0 to 100    
                    if 0 <= marks <= 100:
                        subject[sub] = marks
                        break
                    else:
                        print(" Marks must be between 0 and 100.")


            # add data in function
            manager.addstudent(
                student_id,
                student_name.title(),      
                student_section,
                subject,
            )

       
        elif choice == 2:

            # check students list are empty
            if not manager.students:
                print("No records found. Add a student first.")
            else:
                manager.liststudent()

        
        elif choice == 3:
        
            if not manager.students:
                print("No records found. Add a student first.")

            else:
                while True:
                    try:
                        student_id = int(input("Enter student ID to search: "))
                    except ValueError:
                        print("Invalid ID enter numbers only.")
                        continue

                    if student_id < 0:
                        print("ID must be a positive number.")
                        continue
 
                    # check the ID actually exists before searching
                    if not any(s.student_id == student_id
                               for s in manager.students):
                        print(f"ID {student_id} not found. ")
                        continue
 
                    manager.searchstudent(student_id)
                    break


        elif choice == 4:

            if not manager.students:
                print("No records found. Add a student first.")
            else:
                # ----------- ID INPUT -----------
                while True:
                    try:
                        student_id = int(input("Enter student ID to update: "))
                    except ValueError:
                        print("Invalid ID! Enter numbers only.")
                        continue

                    if student_id <= 0:
                        print("ID must be positive.")
                        continue

                    if not any(s.student_id == student_id for s in manager.students):
                        print(f"ID {student_id} not found.")
                        continue

                    break


                while True:
                    # ----------- UPDATE MENU -----------
                    print("\n-----------Update menu-----------")
                    print("1. Name")
                    print("2. Section")
                    print("3. Subject Marks")
                    print("4. Add New Subject")
                    print("5. Exit")

                    try:
                        update_choice = int(input("Enter choice: "))
                    except ValueError:
                        print("Invalid choice.")
                        continue

                    
                    # ----------- UPDATE NAME -----------
                    if update_choice == 1:
                        name_pattern = r"^[A-Za-z]{2,}(?: [A-Za-z]+)*$"

                        while True:
                            new_name = input("Enter new name: ").strip()

                            if not new_name:
                                print("Name cannot be empty.")
                                continue

                            if not re.fullmatch(name_pattern, new_name):
                                print("Invalid name.")
                                continue

                            if len(new_name) > 50:
                                print("Name too long.")
                                continue

                            break

                        manager.updatestudent(student_id, new_name=new_name.title())

                    # ----------- UPDATE SECTION -----------
                    elif update_choice == 2:
                        while True:
                            new_section = input("Enter new section: ").strip()

                            if not new_section:
                                print("Section cannot be empty.")
                                continue

                            if not re.fullmatch(r"[0-9]{2}\s*[A-Za-z]", new_section):
                                print("Invalid section (e.g. 10A).")
                                continue

                            break

                        manager.updatestudent(student_id, new_section=new_section)

                    # ----------- UPDATE SUBJECT MARKS -----------
                    elif update_choice == 3:
                        sub_pattern = r"^[a-z]{3,}(?: [a-z]{2,})*$"

                        # get student object
                        student_obj = None
                        for s in manager.students:
                            if s.student_id == student_id:
                                student_obj = s
                                break

                        if not student_obj:
                            print("Student not found.")
                            continue


                        while True:

                            sub = input("Enter subject to update: ").strip().lower()

                            # empty check
                            if not sub:
                                print("Subject name cannot be empty.")
                                continue

                            # check subject name only letter    
                            if not re.fullmatch(sub_pattern, sub):
                                print("Subject name must contain letters only ")
                                continue    

                            # find matching subject (first 3 letters match)
                            matched_subject = None
                            for key in student_obj.student_subject:
                                if sub[:3] == key[:3]:
                                    matched_subject = key
                                    break

                            # if no match found ask again
                            if not matched_subject:
                                print("Subject not found. Enter correct subject.")
                                continue

                            # marks input only if subject matched
                            while True:
                                try:
                                    new_marks = int(input(f"Enter new marks for '{matched_subject}' (0–100): "))
                                except ValueError:
                                    print("Invalid marks.")
                                    continue

                                if 0 <= new_marks <= 100:
                                    break
                                else:
                                    print("Marks must be between 0 and 100.")

                            # update using correct subject name
                            manager.updatestudent(
                                student_id,
                                subject_name=matched_subject,
                                new_marks=new_marks
                            )

                            break

                    # ----------- ADD NEW SUBJECT -----------
                    elif update_choice == 4:
                        sub_pattern = r"^[a-z]{3,}(?: [a-z]{2,})*$"
                        while True:
                            sub = input("Enter new subject name: ").strip().lower()

                            # get student object
                            student_obj = None
                            for s in manager.students:
                                if s.student_id == student_id:
                                    student_obj = s
                                    break

                            if not student_obj:
                                print("Student not found.")
                                continue

                            # check subject name only letter    
                            if not re.fullmatch(sub_pattern, sub):
                                print("Subject name must contain letters only ")
                                continue 

                            # exact duplicate check
                            if sub in student_obj.student_subject:
                                print(f"'{sub}' already exists.")
                                continue

                            # similar name check (first 3 letters) 
                            is_duplicate = False
                            for key in student_obj.student_subject:
                                if sub[:3] == key[:3]:
                                    print(f"'{sub}' too similar to '{key}'.")
                                    is_duplicate = True
                                    break

                            if is_duplicate:
                                continue


                            while True:
                                try:
                                    marks = int(input("Enter marks (0–100): "))
                                except ValueError:
                                    print("Invalid marks.")
                                    continue

                                if 0 <= marks <= 100:
                                    break
                                else:
                                    print("Marks must be between 0 and 100.")

                            manager.updatestudent(
                                student_id,
                                subject_name=sub,
                                new_marks=marks
                            )

                            break

                    # ---------------- Exit -----------------         
                    elif update_choice == 5:
                        print("Exit.. update menu..!")
                        break    

                    else:
                        print("Invalid update choice, Enter choice between (1-5).")            
                   
            
        
        elif choice == 5:

            if not manager.students:
                print("No records found. Add a student first.")

            else:
                while True:
                    try:
                        student_id = int(input("Enter student ID to delete: "))
                    except ValueError:
                        print("Invalid ID! enter number only")
                        continue

                    if student_id < 0:
                        print("ID must be positive number.")
                        continue

                    # check the id actually exists before searching
                    if not any(s.student_id == student_id
                               for s in manager.students):
                        print(f"ID {student_id} not found. ")
                        continue

                    manager.deletestudent(student_id)
                    break

        
        elif choice == 6:
 
            # check students[] list.
            if not manager.students:
                print("No records found. Add a student first.")
            else:
                print("\n----------Top performers (GPA > 3.5)-----------")
                manager.top_performer()


        elif choice == 7:
            print("Exit..Grade manager..!")
            break

        else:
            print("Invalid choice, enter a choice between 1 and 6.")


# ----------------------------------------
if __name__ == "__main__":
    main()