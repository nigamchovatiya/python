# top 3 student highest marks
high_marks = [51, 56, 85, 74, 95, 76, 96]
high_marks.sort()
# print( "first highest",high_marks[-1], "second highest ", high_marks[-2], "third highest" ,high_marks[-3])
descmarks = (high_marks[-1], high_marks[-2], high_marks[-3])
print(descmarks)

# third highest mark
marks = [76, 98, 85, 70, 96, 99]
first = marks[0]
second = marks[1]
third = marks[2]

for mark in marks:
    if mark > first:
        third = second
        second = first
        first = mark

    elif mark > second:
        second = mark
    elif mark > third:
        third = mark

print("first: ", first)  # 99
print("second: ", second)  # 98
print("third: ", third)  # 96
