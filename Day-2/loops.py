# ----for and while loop----
for i in range(5):
    print(i)  # 0 1 2 3 4

i = 0
while i <= 4:
    print(i)
    i += 1  # 0 1 2 3 4

range(start, stop, step)
range(5) 0 to 4
range(1, 3) 1 to 3
range(1, 8, 2) 1, 3, 5, 7


fruits = ['apple', 'banana', 'orange']
for index, i in enumerate(fruits):  # easily print index and value
    print(f"{index}, {i}")  # 0,apple 1,banana 2,orange

# ----break and continue-----
for i in range(5):
    if i == 3:
        break    # stop execution
    print(i)  # 0 1 2

for i in range(6):
    if i == 4:
        continue  # skip current iteration value
    print(i)  # 0 1 2 3 5

# ---nested loop----
for i in range(2):
    for j in range(3):
        print(i, j)  # 00 01 02 10 11 12

print("loop exit..")
