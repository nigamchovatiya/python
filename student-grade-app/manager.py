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


    # add record function
    def addstudent(self, student_id: int,
                student_name: str, 
                student_section: str,
                student_subject: dict) -> None:
        
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

        """
        Args:
            None

        Return:
            None    
        """

        if not self.students:
            print("Record are not found.")
            return

        print("List are ------")

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
                f"Grade: {s.cal_grade()}, GPA: {s.cal_gpa()}"
            )


    # search record function
    def searchstudent(self, student_id: int) -> None:

        """
        Args: 
            student_id(int) : take id from a student

        Return:
            None
        """

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
                    f"Grade: {s.cal_grade()}, GPA: {s.cal_gpa()}"
                )

                return 
            
        print("Student not found..")


    # delete record function
    def deletestudent(self, student_id: int) -> None:

        """
        Args: 
            student_id(int) : take id from a student

        Return:
            None    
        """

        for s in self.students:
            if s.student_id == student_id:
                self.students.remove(s)    
                self.save_json() # update json file
                print("student deleted..")
                return
            
        print("Student not found..")    


    # save data in json file
    def save_json(self):

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
                "gpa" : s.cal_gpa()
            })    


        try:
            with open("student.json", 'w') as file:
                json.dump(data, file, indent=4)

            print("data saved in student.json file") 
              
        except Exception as e:
            print("Error time of save file.") 
  
