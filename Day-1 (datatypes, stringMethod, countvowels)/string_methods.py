
# String

# slicing

name = "Hello Team India."
print(name[1:4])  # ell
print(name[:8])  # Hello Te
print(name[4:])  # o Team India.
print(name[:-3])  # Hello Team Ind
print(name[-7:-2])  # Indi
print(name[::2])  # HloTa ni
print(name[::-1])  # .aidnI maeT olleH

# methods
# upper, lower, split, replace, strip, find

name = "Hello India"
print(name.upper())  # HELLO INDIA
print(name.lower())  # hello india
print(name.split())  # split string [hello, india]
print(name.replace('India', 'Teams'))  # hello teams
print(name.find('Hello'))  # return position of a first letter match

name = "--hello--"
print(name.strip('-'))  # hello , extra space,other remove

# f string
team = "India"
winner = "Team is Winner"
print("Match against " + team)  # normal concatination with +

print(f"Last match in {team} and {winner}")  # using fstring

# f string gretting
name = "John"
date = datetime.now()
# date = datetime.now().strftime("%d-%m-%Y")

print(f"Hello Good Evening! My name is {name}. Today is {date} now.")
