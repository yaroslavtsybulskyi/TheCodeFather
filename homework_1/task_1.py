import math


def calculate_circle_area(radius: float) -> float:
    """
    Function to calculate the area of a circle
    :param radius: Radius of circle
    :return:  function is calculating the area of a circle
    """
    return math.pi * radius ** 2


def main():
    """
    Main function for calculation of the area of the circle with radius provided by user input
    """
    user_input = input("Please, enter radius: ")

    try:
        radius = float(user_input)
        if radius <= 0:
            print("Please enter positive number.")
        else:
            print(f"The area of the circle is: {calculate_circle_area(radius):.2f}")
    except ValueError:
        print("Please enter positive number.")


if __name__ == "__main__":
    main()
