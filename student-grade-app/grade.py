"""
  here i create a grade range and 
  according range provide a, b, c
  like grade.
  firstly create a grade file so
  other class use it.
"""

# ----------------------------------------------

# ----------------------------------------------

class Grade:
    """create class grade for return grade."""

    @staticmethod
    def grade_calculator(marks: int) -> str:

        """
        Args:
            marks(int) : take a marks student

        Return:
            str : return grade.
        """

        if marks >= 90:
            return "A+"
        elif marks >= 80:
            return "A"
        elif marks >= 70:
            return "B"
        elif marks >= 50:
            return "C"
        elif marks >= 35:
            return "D"
        else:
            return "F"
        

    @staticmethod
    def grade_gpa(grade: str) -> int:

        """
        Args:
            grade(str) : take a grade from student

        Return:
            int : return gpa number 0-10     
        """

        # dictionary store grade, gpa
        grade_dict = {
            "A+" : 10,
            "A" : 9,
            "B" : 8,
            "C" : 7,
            "D" : 6,
            "F" : 0
        }

        # return gpa according grade
        return grade_dict.get(grade, 0)
        # default 0, else A - 9 gpa take.

        
        
