"""
here i perform a pytest in student_record.py file
"""

# ---------------------------------------------
from student_record import student_record_add
from student_record import student_list
from student_record import student_search
from student_record import student_delete
# ---------------------------------------------


# add
def test_student_record_add() -> None:
    students = []

    # add one student record students list
    student_record_add(students, "john", "1547823690",
                       "85")

    # check 1 students was added 
    assert len(students) == 1

    # check name stored correctly.
    assert students[0]["name"] == "john"


# list
def test_student_list() -> None:
    students = [{"name": "john", "rollno": "1547823690",
                "marks": "85"}]

    # call function and print record
    result = student_list(students)

    assert result is None


# search 
def test_student_search() -> None:
    students = [
        {"name": "john", "rollno": "1547823690",
        "marks": "85"}
    ]

    # call search function and list and name pass
    result = student_search(students, "john", "85")

    # check return student name and marks correct
    assert result["name"] == "john"
    assert result["marks"] == "85"


# delete
def test_student_delete() -> None:
    students = [
        {"name": "john", "rollno": "1547823690",
         "marks": "85"}
    ]    

    student_delete(students, "john")

    # student removed
    assert len(students) == 0


# ----------------------------------------------------- 

def main() -> None:

    test_student_record_add()
    test_student_list()
    test_student_search()
    test_student_delete()


# ------------------------------------------------------ 
  
if __name__ == "__main__":
    main()
