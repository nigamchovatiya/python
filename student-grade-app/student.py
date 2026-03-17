"""
  here i create a student file in that 
  id, name, section and marks and avg,
  grade calculator function.
  grade.py after create a student.py
  depend on grade and represent on student.
"""

# ---------------------------------------------------

from grade import Grade

# ---------------------------------------------------

class Student:
    """create a Student class handle details"""

    def __init__(self, student_id: int, student_name:
                str, student_section: str,
                student_subject: dict) -> None:
        
        """
        Args:
            student_id(int) : take a student id
            student_name(str) : take a student name
            student_section(str) : take a student section
            student_subject(dict) : take a student subject

        Return:
            None 
        """
        
        self.student_id = student_id
        self.student_name = student_name
        self.student_section = student_section
        self.student_subject = student_subject


    def cal_avg(self) -> float:
        """calculate average marks"""

        # marks take
        total = sum(self.student_subject.values())
        # total subject
        count = len(self.student_subject)

        if count > 0:
            return total / count  
        else:
            return 0


    def cal_grade(self) -> str:
        """calculate grade based on average"""

        avg = self.cal_avg()
        return Grade.grade_calculator(avg)


    def cal_gpa(self) -> int:
        """calculate GPA"""

        grade = self.cal_grade()
        return Grade.grade_gpa(grade)