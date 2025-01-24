from math import sqrt


class Vector:
    """
    Multidimensional vector class.
    """

    def __init__(self, *dimensions):
        """
        Multidimensional vector initialization.
        :param dimensions: dimensions of the vector.
        """
        self.dimensions = dimensions

    def __add__(self, other):
        """
        Method to add two same dimensional vectors together.
        :param other: Vector addend.
        :return: the sum of the two vectors - vector.
        """
        if not isinstance(other, Vector):
            raise ValueError("Addends should be Vectors")
        if len(other.dimensions) != len(self.dimensions):
            raise ValueError("Vector dimensions should be the same")
        return Vector(*((a + b) for a, b in zip(self.dimensions, other.dimensions)))

    def __sub__(self, other):
        """
        Method to subtract two same dimensional vectors together.
        :param other: Vector subtrahend.
        :return: Difference between the vectors - vector.
        """
        if not isinstance(other, Vector):
            raise ValueError("Operands should be Vectors")
        if len(other.dimensions) != len(self.dimensions):
            raise ValueError("Vector dimensions should be the same")
        return Vector(*((a - b) for a, b in zip(self.dimensions, other.dimensions)))

    def __mul__(self, scalar):
        """
        Method to multiply scalar and multidimensional vectors.
        :param scalar: scalar to multiply.
        :return: vector multiplied by scalar.
        """
        if not isinstance(scalar, int | float):
            return TypeError("Scalar should be int or float")
        return Vector(*((scalar * a) for a in self.dimensions))

    def get_length(self) -> int | float:
        """
        Method to get the length of the vector.
        :return: the length of the vector.
        """
        return sqrt(sum(x ** 2 for x in self.dimensions))

    def __eq__(self, other) -> bool:
        """
        Method to check if two vectors are equal.
        :param other: another vector.
        :return: boolean indicating if two vectors are equal.
        """
        if not isinstance(other, Vector):
            raise ValueError("Operands should be Vectors")
        if len(other.dimensions) != len(self.dimensions):
            raise ValueError("Vector dimensions should be the same")
        return self.get_length() == other.get_length()

    def __str__(self) -> str:
        """String representation of the vector."""
        return f"Vector{self.dimensions}"


if __name__ == "__main__":
    v1 = Vector(1, 2, 3)
    v2 = Vector(4, 5, 6)

    print(f"Sum of {v1} and {v2} = {v1 + v2}")
    print(f"Difference of {v1} and {v2} = {v1 - v2}")
    print(f"Product of {v1} and 5 = {v1 * 5}")
    print(f"{v1} and {v2} are equal: {v1 == v2}")
