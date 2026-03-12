"""
  simple example inheritance and method overriding
  using Animal, Dog, and Cat classes.
"""

# -----------------------------------------------------

class Animal:
    """Parent class animal."""

    def speak(self) -> None:
        """General animal speaking method."""
        print("Animal is speaking.")

    def __str__(self) -> str:
        return "this is animal."    


class Dog(Animal):
    """Dog class inherit from Animal."""

    def speak(self) -> None:
        """Dog speaking method."""
        print("Dog is speaking.")

    def __str__(self) -> str:
        return "this is dog."


class Cat(Animal):
    """Cat class inherit from Animal."""

    def speak(self) -> None:
        """Cat speaking method."""
        print("Cat is speaking.")

    def __str__(self) -> str:
        return "this is cat."    


d1 = Dog() 
c1 = Cat()

print(d1)  # this is dog.
d1.speak()  # Dog is speaking.

print(c1)  # this is cat.
c1.speak()  # Cat is speaking.
