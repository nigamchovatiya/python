# ----- multiplication table of num-----

for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i} X {j} = {i * j}")

    print(" ")

# ----prime number----
for i in range(2, 51):
    flag = 1
    for j in range(2, i):
        if (i % j == 0):
            flag = 0
            break
    if flag == 1:
        print(i)  # 2 5 7 11 13 17 19 etc..
