# Inheritance 

class Vehicle:  # Parent class

    def wheel(self) -> None: 
        print("has a four wheels.")


class Car(Vehicle):  # Child class
    pass


c1 = Car() # create a child class object
c1.wheel() # has a four wheels.

#-------------------------------------------------------

# super() function

class Animal:

    def __init__(self, name) -> None:
        self.name = name


class Dog(Animal):

    def __init__(self, name, sound) -> None:
        # parent class constructor or method call
        super().__init__(name)
        self.sound = sound


d1 = Dog('tom', 'barking')

print(d1.name) # tom
print(d1.sound) # barking


# ------------------------------------------------------

# method overriding
"""both parent and child class has a same name method,
   override parent class method."""

class Animal:

    def speak(self) -> None:
        print("Animal sound..")


class Dog(Animal):

    def speak(self) -> None:
        print("Dog sound..")

a1 = Animal()
d1 = Dog()
a1.speak() # Animal sound..
d1.speak() # Dog sound..


# ----------------------------------------------------

# isinstace()

class Animal():
    pass

class Dog(Animal):
    pass

d1 = Dog()

print(isinstance(d1, Dog)) # True
print(isinstance(d1, Animal)) # True

                
# ----------------------------------------------------

# Polymorphism

class Cat:

    def eat(self) -> None:
        print("cat is eating.")

class Dog:

    def eat(selt) -> None:
        print("dog is eating.")


cat = Cat()
dog = Dog()

cat.eat() # cat is eating.
dog.eat() # dog is eating.


# ducktyping use for polymorphism
# --------------using - Duck typing ------

class Dog:

    def speak(self) -> None:
        print("dog speaking..")

class Robot:

    def speak(self) -> None:
        print("robot speaking..")


def make_sound(obj) ->None:
    obj.speak()

make_sound(Dog()) # dog speaking..
make_sound(Robot())  # robot speaking..




