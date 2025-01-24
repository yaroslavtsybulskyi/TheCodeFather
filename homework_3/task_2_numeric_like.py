from math import sqrt


class Vector:
    """
    2D Vector class
    """

    def __init__(self, x: int, y: int):
        """
        Constructor of Vector class
        :param x: x coordinate
        :param y: y coordinate
        """
        self.x = x
        self.y = y

    def get_length(self):
        """
        Method that returns the length of the vector
        :return: length of the vector
        """
        return sqrt(self.x ** 2 + self.y ** 2)

    def __add__(self, other):
        """
        Method that adds two vectors together
        :param other: vector to add
        :return: sum of two vectors - new vector
        """
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        return NotImplemented

    def __sub__(self, other):
        """
        Method that subtracts two vectors together
        :param other: vector subtrahend
        :return: the difference of two vectors - new vector
        """
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)
        return NotImplemented

    def __mul__(self, scalar: int):
        """
        Method that multiplies vector and scalar
        :param scalar: int number to multiply
        :return: product of scalar and vector - new vector
        """
        return Vector(self.x * scalar, self.y * scalar)

    def __lt__(self, other) -> bool:
        """
        Method that checks other vector is longer than our vector
        :param other: compare
        :return: result of comparing vectors
        """
        if isinstance(other, Vector):
            return self.get_length() < other.get_length()
        return NotImplemented

    def __eq__(self, other) -> bool:
        """
        Method that checks if vectors are equal
        :param other: vector to compare
        :return: return result of comparing vectors
        """
        if isinstance(other, Vector):
            return self.get_length() == other.get_length()
        return NotImplemented

    def __repr__(self) -> str:
        """String representation of vector"""
        return f"Vector({self.x}, {self.y})"


if __name__ == "__main__":
    v1 = Vector(1, 2)
    v2 = Vector(3, 4)

    print(f"Sum: {v1 + v2}")
    print(f"Difference: {v1 - v2}")
    print(f"Scalar Product: {v1 * 5}")
    print(f"{v2} is greater than {v1}: {v1 < v2}")
    print(f"{v1} is equal to {v2}: {v1 == v2}")
