class Vector:
    """Represent 2d vector."""

    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __add__(self, other: "Vector") -> Vector:
        """Vector Addition."""
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vector") -> Vector:
        """Vector Subtraction."""
        return Vector(self.x - other.x, self.y - other.y)
    
    def __mul__(self, other: "Vector") -> Vector:
        """Vector Multiplication."""
        return Vector(self.x * other.x, self.y * other.y)
    
    def __truediv__(self, other: "Vector") -> Vector:
        """Vector Division."""
        return Vector(self.x / other.x, self.y / other.y)
    
    def __str__(self) -> str:
        return f"({self.x}, {self.y})"
    
    
v1 = Vector(4, 5)
v2 = Vector(2, 4)

# automatically call __add__ 
print("Addition:", v1 + v2) # (6, 9)

# automatically call __sub__
print("Subtraction:", v1 - v2) # (2, 1)

# automatically call __mul__
print("multiplication:", v1 * v2) # (8, 20)

# automatically call __truediv__
print("Division:", v1 / v2) # (2.0, 1.25)