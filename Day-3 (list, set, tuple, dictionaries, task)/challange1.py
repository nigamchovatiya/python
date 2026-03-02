# duplicates name list --------
dup_list = ["nigam", "john", "Doe", "jack", "john", "nigam"]
print("duplicate list = ", dup_list)
new_set = list(set(dup_list))
print("new list = ", new_set)  # remove duplicates

names = ['Nigam', 'John', 'Doe', 'Nigam', 'John']
original = set()
duplicate = set()

for name in names:
    if name in original:  # check name in original
        duplicate.add(name)  # duplicate name store duplicate
    else:
        original.add(name)  # first time store
# print("duplicates name in list:",list(duplicate)) # using list [nigam,john]
print("duplicates name in list:", duplicate)  # using set {nigam,john}
