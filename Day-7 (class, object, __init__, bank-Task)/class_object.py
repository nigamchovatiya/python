# class

class Student:
    pass


#--------------------------------------
# object

class Student:
    pass

s1 = Student() # s1 object
s2 = Student() # s2 object

print(s1)
print(s2)


#---------------------------------------
# __init__

class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

# object create automatically __init__  method call
s4 = Student('bob', 25) 
s5 = Student('john', 20)

print(s4.name) # bob
print(s5.age) # 20


#----------------------------------------
# self keyword

class Car:
    def __init__(self, name):
        self.name = name

c1 = Car('bmw')
print(c1.name) # bmw  


#----------------------------------------
# instance attribute

class Student:
    def __init__(self, name):
        self.name = name

stu1 = Student("Ravi")        
stu2 = Student("Aman")        

# name is instance attribute
print(stu1.name) # Ravi       
print(stu2.name) # Aman       


#-----------------------------------------
# class attribute

class Student:
    
    school = "AB school" # class attribute
    
    def __init__(self):
        pass

su1 = Student()
su2 = Student()

print(su1.school) # AB school
print(su2.school) # AB school


#------------------------------------------
# instance method

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self): # instance method
        print("name:", self.name)
        print("marks:", self.marks)


stu1 = Student('john', 95)

stu1.display() # name: john, marks: 95    

#-------------------------------------------
# __str__ method

class Car:

    def __init__(self,model):
        self.model = model

    def __str__(self): 
        return f"The {self.model} model has launched in 2022."
    
    
my_car = Car('XUV700')
print(my_car) # The xuv700 model has launch in 2022.


# without str method
# class Car:

#     def __init__(self,model):
#         self.model = model

    
# my_car = Car('XUV700')
# print(my_car) # <__main__.Car object at 0x000002116AC98EC0>
