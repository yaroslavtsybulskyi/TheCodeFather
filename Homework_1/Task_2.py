class Rectangle:
    """
    Class Rectangle represents rectangle, which has width and height.
    """

    width = 0.0
    height = 0.0

    def __init__(self, width: float, height: float):
        """
        Constructor for rectangle.
        :param width: width of rectangle.
        :param height:  height of rectangle.
        """
        self.width = width
        self.height = height

    def area(self) -> float:
        """
        Calculates the area of rectangle.
        :return: function returns area of rectangle
        """
        return self.width * self.height

    def perimeter(self) -> float:
        """
        Calculates the perimeter of rectangle.
        :return: function returns perimeter of rectangle
        """
        return 2 * (self.width + self.height)

    def is_square(self) -> bool:
        """
        Checks if rectangle is square.
        :return: function returns whether rectangle is square
        """
        return self.width == self.height

    def resize(self, new_width, new_height):
        """
        Resizes rectangle.
        :param new_width: new width of rectangle.
        :param new_height: new height of rectangle.
        :return: function returns resized rectangle
        """
        self.width = new_width
        self.height = new_height

    def __str__(self) -> str:
        """
        Represents rectangle.
        :return: function returns string representation of rectangle
        """
        return f'Rectangle(Width: {self.width}, Height: {self.height})'


if __name__ == '__main__':
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
