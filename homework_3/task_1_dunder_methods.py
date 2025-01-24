class Fraction:
    """
    Class Fraction
    """

    def __init__(self, numerator: int, denominator: int):
        """
        Constructor of fraction
        :param numerator: numerator of the fraction
        :param denominator: denominator of the fraction
        """
        if denominator == 0:
            raise ValueError("Denominator cannot be 0")

        self.numerator = numerator
        self.denominator = denominator

    def __add__(self, other):
        """
        methods that allow addition of two fractions
        :param other: fraction addend
        :return: the sum of the two fractions
        """
        if isinstance(other, Fraction):
            nominator = self.numerator * other.denominator + self.denominator * other.numerator
            denominator = self.denominator * other.denominator
            return Fraction(nominator, denominator)
        return NotImplemented

    def __sub__(self, other):
        """
        methods that allow subtraction of two fractions
        :param other: fraction subtrahend
        :return: difference of the two fractions
        """
        if isinstance(other, Fraction):
            nominator = self.numerator * other.denominator - self.denominator * other.numerator
            denominator = self.denominator * other.denominator
            return Fraction(nominator, denominator)
        return NotImplemented

    def __mul__(self, other):
        """
        methods that allow multiplication of two fractions
        :param other: fraction that will be multiplied
        :return: product of two fractions
        """
        if isinstance(other, Fraction):
            nominator = self.numerator * other.numerator
            denominator = self.denominator * other.denominator
            return Fraction(nominator, denominator)
        return NotImplemented

    def __truediv__(self, other):
        """
        methods that allow division of two fractions
        :param other: fraction divisor
        :return: quotient of two fractions
        """
        if isinstance(other, Fraction):
            nominator = self.numerator * other.denominator
            denominator = self.denominator * other.numerator
            return Fraction(nominator, denominator)
        return NotImplemented

    def __repr__(self) -> str:
        """String representation of fraction"""
        return f"{self.numerator}/{self.denominator}"


if __name__ == "__main__":
    f1 = Fraction(4, 2)
    f2 = Fraction(3, 5)
    print(f1)
    print(f2)
    print(f"Sum: {f1 + f2}")
    print(f"Difference: {f1 - f2}")
    print(f"Product: {f1 * f2}")
    print(f"Quotient: {f1 / f2}")
