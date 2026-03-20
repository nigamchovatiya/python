"""
  here i create a manager file that 
  manage marks add, list, search and 
  delete.
  student.py after create manager.py
  manage list of student. 
"""

# --------------------------------------------------

from student import Student
import json
 
# --------------------------------------------------

class StudentManager:
    """create StudentManager class handle crud op."""

    def __init__(self) -> None:
        # empty list students
        self.students = []
        # self.load_json()


    # add record function
    def addstudent(self, student_id: int,
                student_name: str, 
                student_section: str,
                student_subject: dict) -> None:
        
        """add student in list"""
        
        """
        Args:
            student_id(int) : take a id from student
            student_name(str) : take a name from student
            student_section(str) : take a section from student
            student_subject(dict) : take a subject from student

        Return:
            None    
        """

        student =  Student(student_id, student_name,
                        student_section, student_subject) 

        self.students.append(student)

        
        self.save_json() # save data in json file
        print("record added successfully.")
        


    # list record function
    def liststudent(self) -> None:
        """print list of student"""

        """
        Args:
            None

        Return:
            None    
        """

        if not self.students:
            print("Record are not found.")
            return

        print("\n----------------List are-----------------\n")

        for s in self.students:
            print(
                f"Id: {s.student_id}, Name: {s.student_name}, "
                f"Section: {s.student_section}"
            )

            print("Subjects & Marks:")

            for sub, marks in s.student_subject.items():
                print(f"  {sub}: {marks}")

            print(
                f"Average: {s.cal_avg():.2f}, "
                f"GPA: {s.cal_gpa()}, Grade: {s.cal_grade()}"
            )
            print("\n-------------------------------------------\n")


    # search record function
    def searchstudent(self, student_id: int) -> None:
        """search student based on id"""

        """
        Args: 
            student_id(int) : take id from a student

        Return:
            None
        """

        print("\n---------------Search List------------------\n")
        for s in self.students:
            if s.student_id == student_id:

                print(
                    f"Id: {s.student_id}, Name: {s.student_name}, "
                    f"Section: {s.student_section}"
                ) 

                print("Subjects:")
                for sub, marks in s.student_subject.items():
                    print(f"  {sub}: {marks}")

                print(
                    f"Average: {s.cal_avg():.2f}, "
                    f"GPA: {s.cal_gpa()}, Grade: {s.cal_grade()}"
                )

                print("\n-------------------------------------------\n")

                return 
            
        print("Student id not found..")


    # update record function    
    def updatestudent(self, student_id: int,
                  new_name: str = None,
                  new_section: str = None,
                  new_subject: dict = None,
                  subject_name: str = None,
                  new_marks: int = None) -> None:
        """update student details including marks"""

        for s in self.students:
            if s.student_id == student_id:

               # update name
                if new_name:
                    s.student_name = new_name

                # update section
                if new_section:
                    s.student_section = new_section

                # update full subject dict
                if new_subject:
                    s.student_subject = new_subject

                #  update single subject marks
                if subject_name and new_marks is not None:

                    subject_name = subject_name.lower()

                    # if subject exists  update
                    if subject_name in s.student_subject:
                        s.student_subject[subject_name] = new_marks
                        print(f"{subject_name} marks updated.")

                    # if not exists add new subject
                    else:
                        s.student_subject[subject_name] = new_marks
                        print(f"{subject_name} added with marks.")

                self.save_json()

                print("Record updated successfully.")

                # show updated data
                print("\n----------------Update data---------------\n")

                print(
                    f"Id: {s.student_id}, Name: {s.student_name}, "
                    f"Section: {s.student_section}"
                )

                print("Subjects & Marks:")
                for sub, marks in s.student_subject.items():
                    print(f"  {sub}: {marks}")

                print(
                    f"Average: {s.cal_avg():.2f}, "
                    f"GPA: {s.cal_gpa()}, Grade: {s.cal_grade()}"
                )

                print("\n-------------------------------------------\n")

                return

        print(f"Student ID {student_id} not found.")


    # delete record function
    def deletestudent(self, student_id: int) -> None:
        """delete student based on id"""

        """
        Args: 
            student_id(int) : take id from a student

        Return:
            None    
        """
        print("\n-----------------Delete----------------\n")

        for s in self.students:
            if s.student_id == student_id:
                self.students.remove(s)    
                self.save_json() # update json file
                print("Student deleted..")
                return
            
        print("Student id not found..")    


    # save data in json file
    def save_json(self) -> None:
        """store data in json file"""

        """
        Args:
            None

        Return:
            None    
        """
        # assign empty list
        data = []

        for s in self.students:
            data.append({
                "id": s.student_id,
                "name": s.student_name,
                "section": s.student_section,
                "subjects": s.student_subject,
                "average": s.cal_avg(),
                "grade" : s.cal_grade(),
                "gpa" : s.cal_gpa(),
            })    


        try:
            with open("student.json", 'w') as file:
                json.dump(data, file, indent=4)

            print("Data saved in student.json file") 
              
        except Exception as e:
            print("Error time of save file.")   


    def load_json(self) -> None:
        """load json data"""

        try:
            with open("student.json", "r") as file:
                data = json.load(file)
                # print(data)

            for d in data:
                student = Student(d['id'], d['name'], d['section'], d['subjects'])
                self.students.append(student)

            # print("Data loaded successfully.")  


        except Exception as e:
            print("Unexpected error:", e)   
  

    # top performer gpa above 3.5
    def top_performer(self) -> None:
        """print top performer student gpa > 3.5"""

        """
        Args: 
            None

        Return:
            None    
        """
        # record empty  
        if not self.students:
            print("Record are not found.")
            return
        
        found = False

        # check students list 
        for s in self.students:
            # gpa > 3.5
            if float(s.cal_gpa()) > 3.5:
                found = True

                print(
                    f"Id: {s.student_id}, Name: {s.student_name}, "
                    f"Section: {s.student_section}"
                )

                print("Subjects & Marks:")

                for sub, marks in s.student_subject.items():
                    print(f"  {sub}: {marks}")

                print(
                    f"Average: {s.cal_avg():.2f}, "
                    f"GPA: {s.cal_gpa()}, Grade: {s.cal_grade()}"
                )

                print("\n-------------------------------------------\n")


        if not found:
            print("Not top performer found in list.")
        