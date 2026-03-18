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
        """grade given according to marks"""

        """
        Args:
            marks(int) : take a marks student

        Return:
            str : return grade.
        """

        if marks >= 97:
            return "A+"
        elif marks >= 93:
            return "A"
        elif marks >= 90:
            return "A-"
        elif marks >= 88:
            return "B+"
        elif marks >= 83:
            return "B"
        elif marks >= 80:
            return "B-"
        elif marks >= 75:
            return "C"
        elif marks >= 65:
            return "D"
        else:
            return "F"
        

    @staticmethod
    def grade_gpa(grade: str) -> int:
        """gpa given according to grade"""

        """
        Args:
            grade(str) : take a grade from student

        Return:
            int : return gpa number 0-10     
        """

        # dictionary store grade, gpa
        grade_dict = {
            "A+" : 4.0,
            "A" : 4.0,
            "A-" : 3.7,
            "B+" : 3.3,
            "B" : 3.0,
            "B-" : 2.7,
            "C" : 2.0,
            "D" : 1.2,
            "F" : 0
        }

        # return gpa according grade
        return grade_dict.get(grade, 0)
        # default 0, else A - 9 gpa take.

        
        
