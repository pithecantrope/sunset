import math

class Rectangle:
        def __init__(self, w, h): self.w, self.h = w, h

        def area(self): return self.w * self.h
        def perimeter(self): return 2 * (self.w + self.h)
        def display(self):
                print(f"Rectangle: {self.w}x{self.h}")
                print(f"Area: {self.area()}, Perimeter: {self.perimeter()}")

class Circle:
        def __init__(self, r): self.r = r

        def area(self): return math.pi * self.r ** 2
        def circumference(self): return 2 * math.pi * self.r
        def display(self):
                print(f"Circle: Radius {self.r}")
                print(f"Area: {self.area():.2f}, Circumference: {self.circumference():.2f}")

if __name__ == "__main__":
        rect = Rectangle(5, 10)
        circ = Circle(7)
        rect.display()
        circ.display()
