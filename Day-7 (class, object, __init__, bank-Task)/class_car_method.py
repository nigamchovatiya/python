"""
  Simple Car class example with attributes and methods.
"""

# -------------------------------------------------------------------

class Car:
    """A Car class represent a car."""

    def __init__(self, make, model, year) -> str:
        """Intialize car attributes."""
        self.make = make
        self.model = model
        self.year = year

    def __str__(self) -> str:
        return f"{self.make}, {self.model}, {self.year}"    

    def accelerate(self) -> str:
        """Display accelerate message."""
        print(f"{self.make} {self.model} accelerate up to 280km/h.")

    def brake(self) -> str:
        """Display brake message."""
        print(f"{self.model} in this model has ADAS brake system.")    


car1 = Car('BMW', 'M-series', 2016)
print(car1) # BMW, M-series, 2016

# print("Cars:", car1.make, car1.model, car1.year) # BMW M-series 2016
car1.accelerate() # BMW M-series accelerate up to 280km/h.
car1.brake() # M-series in this Model has ADAS brake system.
