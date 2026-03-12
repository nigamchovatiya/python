"""
  simple example inheritance, method overriding
  and @property validation using Animal, Dog, 
  and Cat classes.
"""

# -----------------------------------------------------

class Animal:
    """Parent class Animal."""

    def __init__(self, name: str):
        self.name = name   # calls setter

    #Getter
    @property
    def name(self) -> str:
        """Getter method."""
        return self._name

    #Setter
    @name.setter
    def name(self, value: str) -> None:
        """Setter with validation."""
        if not isinstance(value, str):
            raise ValueError("Name must be a string.")
        self._name = value

    def speak(self) -> None:
        """General animal speaking method."""
        print("Animal is speaking.")

    def __str__(self) -> str:
        return f"Animal Name: {self.name}"


class Dog(Animal):
    """Dog class inherit from Animal."""

    def speak(self) -> None:
        print(f"{self.name} says: Woof!")


class Cat(Animal):
    """Cat class inherit from Animal."""

    def speak(self) -> None:
        print(f"{self.name} says: Meow!")


# -----------------------------------------------------

d1 = Dog("Tommy")
c1 = Cat("Kitty")

print(d1) # Animal Name: Tommy
d1.speak() # Tommy says: Woof!

print(c1) # Animal Name: Kitty
c1.speak() # Kitty says: Meow!
