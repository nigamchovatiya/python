from datetime import datetime

# print("hello")
# print("Nigam Chovatiya")
# print("I am a 21 year old.")


name = "Nigam"
age = "21"
currentdate = datetime.now()

print("hello my name is " + name + " and I am " + age + " years old.")
print("Today date is: ",currentdate)


#data types
x = 1
print(x, type(x))

x = "nigam"
print(x, type(x))

x = True
print(x, type(x))

x = 5.0
print(x, type(x))

x = None
print(x, type(x))


#String 

#slicing

name = "Hello Team India."
print(name[1:4]) # ell
print(name[:8]) # Hello Te
print(name[4:]) # o Team India.
print(name[:-3]) # Hello Team Ind
print(name[-7:-2]) #  Indi
print(name[::2]) # HloTa ni
print(name[::-1]) # .aidnI maeT olleH

#methods
#upper, lower, split, replace, strip, find

name = "Hello India"
print(name.upper()) # HELLO INDIA
print(name.lower()) # hello india
print(name.split()) # split string [hello, india]
print(name.replace('India', 'Teams')) # hello teams
print(name.find('Hello')) # return position of a first letter match

name = "--hello--"
print(name.strip('-')) # hello , extra space,other remove

# f string
team = "India"
winner = "Team is Winner"
print("Match against " + team) # normal concatination with + 

print(f"Last match in {team} and {winner}") # using fstring

# f string gretting
name = "John"
date = datetime.now()
# date = datetime.now().strftime("%d-%m-%Y")

print(f"Hello Good Evening! My name is {name}. Today is {date} now.")

# Count vowels
char = "nigam Ae"
vowel = "aeiouAEIOU"
count=0
for n in char:
   if n in vowel:
       count = count+1
       print(n) # (i,a,A,e)
       
print("total vowel in ",count)  # 4     