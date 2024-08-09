import math

class Vector:
    def __init__(self, *components):
        self.components = list(components)
    
    def __add__(self, other):
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must have the same dimension for addition")
        return Vector(*[a + b for a, b in zip(self.components, other.components)])
    
    def __sub__(self, other):
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must have the same dimension for subtraction")
        return Vector(*[a - b for a, b in zip(self.components, other.components)])
    
    def dot(self, other):
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must have the same dimension for dot product")
        return sum(a * b for a, b in zip(self.components, other.components))
    
    def magnitude(self):
        return math.sqrt(sum(x ** 2 for x in self.components))
    
    def __repr__(self):
        return f"Vector({', '.join(map(str, self.components))})"

# Example usage:
v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)

print("v1 + v2 =", v1 + v2)
print("v1 - v2 =", v1 - v2)
print("v1 . v2 =", v1.dot(v2))
print("|v1| =", v1.magnitude())
