# ---- List -----
# create list
create_list = ["nigam", 1, True, 4.5]
print(create_list)  # nigam,1,True,4.5

create_list[2] = "string"  # add a 2 index string

# index access
print(create_list[3])  # 4.5

# append
create_list.append(5)
print(create_list)  # add 5 in list last position

# pop
create_list.pop()
print(create_list)  # delete last element of list 5

# remove
create_list.remove(1)
print(create_list)  # remove a perticular element 1

# del
del create_list[0]
print(create_list)  # delete element with index value

# sort
sort_list = [34, 4, 5, 2, 1]
sort_list.sort()
print(sort_list)  # [1,2,4,5,34]

# slice
new_list = ['nigam', 21, 12, 'True', 'False']
# old_list = new_list[1:4]
print(new_list[1:4])  # 21,12,true
print(new_list[::2])  # nigam,12,false

# list comprehensive
new_list = [1, 2, 3, 4, 7, 8]
even = [num for num in new_list if num % 2 == 0]
print(even)  # filter even number with list comprehensive

odd = [num for num in new_list if num % 2 != 0]
print(odd)


# new list
num = [1, 3, 5, 7]
square = [x * x for x in num]
print(square)  # 1,9,25,49

# find max
num = [1, 56, 78, 9, 60]
# num.sort()
largest = 0
for x in num:
    if largest < x:
        largest = x
print(largest)  # 78

l1 = [2, 45, 1, 3, 4]
l1.sort()
print(l1[-1])  # 45
