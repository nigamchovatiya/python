# Advanced OOP

# __str__()

class Student:

    def __init__(self, name: str) -> None:
        self.name = name

    def __str__(self) -> str:
        return f"{self.name} Goodmorning.."


s1 = Student('John')
print(s1) # John Goodmorning..       


# __repr__()

class Car:

    def __init__(self, name: str, brand: str) -> None:
        self.name = name
        self.brand = brand

    def __repr__(self) -> str:
        return f"Car('{self.name}', '{self.brand}')"


c1 = Car('M8', 'BMW')
print(c1) # Car('M8', 'BMW')       


# __len__()

class A:

    def __init__(self, name: str) -> None:
        self.name = name

    def __len__(self) -> int:
        return len(self.name)


a1 = A('john')
a2 = A(['john', 'doe', 'kumar'])

print(len(a1)) # 4
print(len(a2)) # 3


# __eq__()

class B:

    def __init__(self, brand: str) -> None:
        self.brand = brand 

    def __eq__(self, other: str) -> bool:
        return self.brand == other.brand
    
b1 = B('Toyota')    
b2 = B('BMW')    
b3 = B('Toyota')

print(b1 == b2) # False
print(b1 == b3) # True


# @property decorator

class A:

    def __init__(self, num1: int) -> None:
        self.num1 = num1

    @property
    def square(self):
        return self.num1 ** 2

a1 = A(2)
#print(a1.square()) Without property decorator.
print(a1.square) # 4   


# static method

class B:

    @staticmethod
    def add(a: int, b: int) -> int:
        return a + b
    

print(B.add(5, 7)) # 12


# class method

class C:

    school = "abc school" # class variable

    def __init__(self) -> None:
        pass

    @classmethod
    def change_school(cls, new_school: str) -> None:
        # class variable change for all object
        cls.school = new_school 

c1 = C()
c1.change_school('zxy school')
print(c1.school)     


# input validation

class Person:

    def __init__(self, age: int) -> None:
        self.age = age # call setter automatically

    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, value):

        if value < 0:
            print("age can't be negative..")
        else:
            self._age = value


p1 = Person(18)
print(p1.age) # 18

p2 = Person(-25)
print(p2.age) # error: value can't be negative..

