# ---Grade Calculator---
marks = int(input("enter a marks: "))

if marks >= 95:
    print("Grade A+")
elif marks >= 85:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 65:
    print("Grade C")
elif marks >= 45:
    print("Grade D")
else:
    print("Grade F")
