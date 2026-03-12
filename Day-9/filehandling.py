"""
  File handling Example with append, read, readline,
  readlines, and with statement.
"""

"""--------------write to a file --------------------"""

file = open("data.txt", "w")

file.write("this is python\n")
file.write("python is easy language.")

file.close()


"""-----------------Append a data ---------------------"""

file = open("data.txt", "a")

file.write("\nthis is append data in end.")
file.close()


""" ------------read a file -------"""

file = open("data.txt", "r")

content = file.read()
print(content)
file.close()


"""--------------readline() --------------------"""

file = open("data.txt", "r")

readcont = file.readline() # read single line
print(readcont) # this is python
file.close()


"""----------------readlines() -----------------"""

file = open("data.txt", "r")

readcont = file.readlines() # read muliple lines and print in list
print(readcont) 
file.close()


"""-------------------- with statement ------------"""

# no need a close a file 
# read file
with open('data.txt', 'r') as file:
    data = file.read()
    print(data)

# write file
with open('data.txt', 'w') as file:
    file.write("\nthis is with statement write.")


