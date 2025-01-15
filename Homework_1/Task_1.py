import math


def calculate_circle_area(radius):
    return math.pi * radius ** 2


user_input = input("Please, enter radius: ")

try:
    radius = float(user_input)
    if radius <= 0:
        print("Please enter positive number.")
    else:
        print(f"The area of the circle is: {calculate_circle_area(radius)}")
except ValueError:
    print("Please enter positive number.")
