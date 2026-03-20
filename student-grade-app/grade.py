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
    def grade_calculator(gpa: float) -> str:
        """grade given according to gpa"""

        """
        Args:
            marks(int) : take a gpa 

        Return:
            str : return grade.
        """

        if gpa >= 3.5:
            return "A"
        elif gpa >= 3.0:
            return "B"
        elif gpa >= 2.5:
            return "C"
        elif gpa >= 2.0:
            return "D"
        else:
            return "F"
        

        
