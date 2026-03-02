# ----------------------set operation -------------
set1 = {1, 2, 4, 5}
set2 = {5, 6, 7, 8}
print(set1 | set2)  # union op.
print(set1 & set2)  # intersection op.
print(set1 - set2)  # diffrence op.


list1 = [1, 2, 3, 1, 2, 3, 4, 5, 6, 6]
set1 = set(list1)
print(set1)  # retrun set output

list2 = list(set(set1))
print(list2)  # return list [] output

# ------------------tuple coordinates --------
point = (10, 20)
print("X:", point[0])
print("Y:", point[1])
