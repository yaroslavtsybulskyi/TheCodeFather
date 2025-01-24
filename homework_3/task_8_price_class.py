class Price:
    """
    Class Price
    """

    def __init__(self, price: int | float, currency: str = 'UAH') -> None:
        """
        Constructor of Price
        :param price: amount of price
        :param currency: currency of price
        """
        if not isinstance(price, int | float):
            raise ValueError('Price should be a number')
        self.price = round(price, 2)
        self.currency = currency

    def __add__(self, other):
        """
        Method for addition of two prices
        :param other: another price to add
        :return: sum of the prices
        """
        if not isinstance(other, Price):
            raise TypeError('Both addends should be of type Price')
        if not self.currency == other.currency:
            raise ValueError('Currencies do not match')
        return Price(self.price + other.price)

    def __sub__(self, other):
        """
        Method for subtraction of two prices
        :param other: Subtrahend
        :return: the difference between the two prices
        """
        if not isinstance(other, Price):
            raise TypeError('Both operands should be of type Price')
        if not self.currency == other.currency:
            raise ValueError('Currencies do not match')
        return Price(self.price - other.price)

    def __eq__(self, other) -> bool:
        """
        Method that shows that two prices are equal
        :param other: other price to compare
        :return: boolean value indicating if two prices are equal
        """
        if not isinstance(other, Price):
            raise TypeError('Both operands should be of type Price')
        if not self.currency == other.currency:
            raise ValueError('Currencies do not match')
        return self.price == other.price

    def __lt__(self, other) -> bool:
        """
        Method for comparing two prices
        :param other: other price to compare
        :return: boolean value indicating if the first price is less than the second
        """
        if not isinstance(other, Price):
            raise TypeError('Both operands should be of type Price')
        if not self.currency == other.currency:
            raise ValueError('Currencies do not match')
        return self.price < other.price

    def __gt__(self, other):
        """
        Method for comparing two prices
        :param other: other price to compare
        :return: bool value indicating if the first price is greater than the second
        """
        if not isinstance(other, Price):
            raise TypeError('Both operands should be of type Price')
        if not self.currency == other.currency:
            raise ValueError('Currencies do not match')
        return self.price > other.price

    def __str__(self) -> str:
        """string representation of price"""
        return f'Price: {self.price} {self.currency}'

    @classmethod
    def from_cents(cls, cents: int, currency: str = 'UAH'):
        """
        Class method that creates a price object from cents
        :param currency: currency of price
        :param cents: amount of cents
        :return: price object
        """
        if not isinstance(cents, int):
            return ValueError('Cents should be an integer')
        return cls(cents / 100, currency)

    def convert_to(self, exchange_rate: int | float, currency: str = 'USD'):
        """
        Convert to another currency
        :param exchange_rate: exchange rate
        :param currency: currency to convert to
        :return: price in another currency
        """
        if not isinstance(exchange_rate, int | float):
            raise ValueError('Exchange rate should be an integer or float')
        return Price(self.price * exchange_rate, currency)


if __name__ == '__main__':
    p1 = Price(1.567, 'UAH')
    p2 = Price(100.47, 'UAH')

    print(f"Sum: {p1 + p2}")
    print(f"Difference: {p1 - p2}")
    print(f"Prices are equal: {p1 == p2}")
    print(f"First {p1} is higher than second {p2} : {p1 > p2}")
    print("Convert to USD - exchange rate = 0.024")
    print(f"{p1.convert_to(exchange_rate=0.024)}")
    print(f"{p2.convert_to(exchange_rate=0.024)}")

    p3 = Price.from_cents(3000)
    print(p3)
    print(f"{p3.convert_to(exchange_rate=0.024)}")
