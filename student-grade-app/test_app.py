"""
test_app file test student grade manager all 
function. 
"""

# -----------------------------------------------

import pytest
from student import Student
from manager import StudentManager
from grade import Grade

# -----------------------------------------------


"""student class test"""

def test_cal_avg() -> None:
    """test cal_avg() function"""

    # create student class object
    s = Student(1, "john", "A", {"eng": 90, "math": 80})
    # check resultant output return true
    assert s.cal_avg() == 85


def test_cal_grade() -> None:
    """test cal_grade() function"""

    s = Student(2, "john", "B", {"maths": 95})
    assert s.cal_grade() == "A"


def test_cal_gpa() -> None:
    """test cal_gpa() function"""

    s = Student(3, "alice", "A", {"maths": 95})
    assert s.cal_gpa() == 4.0        


# ------------------------------------------------

"""grade class test"""

def test_grade_calculator() -> None:
    """test grade_calculator() function"""

    g = Grade()
    assert g.grade_calculator(90) == "A-"


def test_grade_gpa() -> None:
    """test grade_gpa() function"""

    g = Grade()
    assert g.grade_gpa("B") == 3.0    


# -------------------------------------------------

"""manager class test""" 

# create new studentmanager objects

@pytest.fixture
def manager() -> object:
    """StudentManager class object create"""

    return StudentManager()


# add student test
def test_addstudent(manager) -> None:
    """test addstudent() function print result"""

    # add 1 student
    manager.addstudent(1, "john", "B", {"maths": 95})

    # check len of students list
    assert len(manager.students) == 1


# list student test
def test_liststudent(manager, capsys) -> None:
    """test liststudent() function print result"""

    manager.addstudent(1, "john", "B", {"maths": 90})

    # list print
    manager.liststudent()

    # capture printed output
    captured = capsys.readouterr()

    # check john in capture data
    assert "john" in captured.out


# search student test
def test_searchstudent(manager, capsys) -> None:
    """test searchstudent() function print result"""

    manager.addstudent(1, "john", "B", {"maths": 90})

    # search id given
    manager.searchstudent(1)

    captured = capsys.readouterr()

    assert "john" in captured.out


# delete student test
def test_deletestudent(manager, capsys) -> None:
    """test deletestudent() function print result"""

    manager.addstudent(1, "john", "B", {"maths": 90})    

    manager.deletestudent(1)

    captured = capsys.readouterr()

    # check message print
    assert "deleted" in captured.out
    # check students list empty
    assert len(manager.students) == 0


# top_performer test
def test_top_performer(manager, capsys) -> None:
    """test top_performer() function print result"""

    # 2 record add
    manager.addstudent(1, "Alice", "A", {"maths": 95})
    manager.addstudent(2, "John", "B", {"maths": 70})

    # function call
    manager.top_performer()

    # printed output captured
    captured = capsys.readouterr()

    # check highest scoring student
    assert "Alice" in captured.out   



"""
without fixture every time object create and
reapeat in every code
"""

"""
def test_addstudent() -> None:
    manager = StudentManager()
    manager.addstudent(1, "john", "B", {"marks": 92})

    assert len(manager.students) == 1

def test_liststudent(capsys) -> None:
    manager = StudentManager()
    manager.addstudent(1, "john", "B", {"marks": 92})

    manager.liststudent()
    captured = capsys.readouterr()
    assert "john" in captured.out
"""