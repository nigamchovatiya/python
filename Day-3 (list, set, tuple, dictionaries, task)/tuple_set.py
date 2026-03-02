# -----------------tuple and set-----------

t1 = ("nigam", 1, True)
print(t1)  # nigam,1,true
print(t1[0])  # nigam

t1[0] = "Chovatiya"
print(t1)  # error can't modify

# ---------------------- set-------------
s1 = {1, 2, 3, 4, 5, 6, 1, 2, 3}
print(s1)  # 1,2,3,4,5,6 (remove duplicates & automatically order set)

s1.add(7)
s1.remove(6)
print(s1)
