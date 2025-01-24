class ProductWithGetSet:
    """
    Product class with get-set.
    """

    def __init__(self, name: str, price: int | float) -> None:
        """
        Constructor.
        :param name: name of the product.
        :param price: price of the product.
        """
        self._name = name
        self._price = price

    def get_price(self) -> int | float:
        """gets the price of the product."""
        return self._price

    def set_price(self, price: int | float) -> None:
        """
        sets the price of the product.
        :param price: price of the product.
        """
        if price < 0:
            raise ValueError("Price cannot be negative")
        self._price = price

    def __str__(self) -> str:
        """string representation of the product."""
        return f"{self._name} {self._price}"


class ProductWithProperty:
    """
    Product class with property.
    """

    def __init__(self, name: str, price: int | float) -> None:
        """
        Constructor.
        :param name: name of the product.
        :param price: price of the product.
        """
        self._name = name
        self._price = price

    @property
    def price(self) -> int | float:
        """gets the price of the product."""
        return self._price

    @price.setter
    def price(self, price: int | float) -> None:
        """
        sets the price of the product.
        :param price: price of the product.
        """
        if not isinstance(price, int | float):
            raise TypeError("Price must be a number")
        if price < 0:
            raise ValueError("Price cannot be negative")
        self._price = price

    def __str__(self) -> str:
        """string representation of the product."""
        return f"{self._name} {self._price}"


class PriceDescriptor:
    """Price Descriptor Class"""

    def __get__(self, instance, owner):
        """Getter."""
        return instance.__dict__['price']

    def __set__(self, instance, value):
        """Setter."""
        if not isinstance(value, int | float):
            raise ValueError("Value must be numeric")
        if value < 0:
            raise ValueError("Value must be positive")
        instance.__dict__['price'] = value


class ProductWithDescriptor:
    """Product class with descriptor."""

    price = PriceDescriptor()

    def __init__(self, name: str, price: int | float) -> None:
        """
        Constructor.
        :param name: name of the product.
        :param price: price of the product.
        """
        self.name = name
        self.price = price

    def __str__(self) -> str:
        """string representation of the product."""
        return f"{self.name} {self.price}"


if __name__ == "__main__":
    p1 = ProductWithGetSet("Book", 15.2)
    print(p1)
    p1.set_price(10)
    print(p1)
    print('*****' * 10)
    p2 = ProductWithProperty("Movie", 16.6)
    print(p2)
    p2.price = 10
    print(p2)
    print('*****' * 10)
    p3 = ProductWithDescriptor("Stock", 115.2)
    print(p3)
    p3.price = 202
    print(p3)
