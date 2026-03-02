
# ---- star pattern-----

print("\n\nPattern 1")
n = 5
for i in range(i, n + 1):
    for j in range(i):
        print("*", end="")
    print()

n = 5
for i in range(5, 0, -1):  
    for j in range(i):
        print("*", end="")
    print()

print("\n\nPattern 2")
n = 5
for i in range(1, n + 1):
    for j in range(1, n + 1 - i):
        print(" ", end="")
    for j in range(1, i + 1):
        print("*", end="")
    print("")

print("\n\nPattern 3")
n = 5
for i in range(n, 0, -1):
    for j in range(1, i + 1):
        print("*", end="")
    print("")

print("\n\nPattern 4")
n = 5
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, " ", end="")
    print("")

print("\n\nPattern 5")
n = 5
k = 1
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(k, " ", end="")
        k = k + 1
    print("")
