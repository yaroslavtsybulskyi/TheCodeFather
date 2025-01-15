class Rectangle:
    width = 0.0
    height = 0.0

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def is_square(self):
        return self.width == self.height

    def resize(self, new_width, new_height):
        self.width = new_width
        self.height = new_height

    def __str__(self):
        return f'Rectangle(Width: {self.width}, Height: {self.height})'

rect = Rectangle(100, 100)

print("Area: ", rect.area())
print("Perimeter: ", rect.perimeter())
print("Is square: ", rect.is_square())
print(rect)

rect.resize(140, 120)

print("Area: ", rect.area())
print("Perimeter: ", rect.perimeter())
print("Is square: ", rect.is_square())
print(rect)
