CURRENCY_RATES = {
    'UAH': 1.0,
    'USD': 40.5,
    'EUR': 50.0
}


class CurrencyDescriptor:
    """Currency descriptor class"""

    def __get__(self, instance, owner):
        """Getter"""
        return instance.__dict__['currency']

    def __set__(self, instance, value):
        """Setter"""
        if not isinstance(value, str):
            raise TypeError('Value must be a string')
        if value.upper() not in CURRENCY_RATES:
            raise ValueError('Value must be in currency rates')
        instance.__dict__['currency'] = value.upper()

    def convert_currency(self, price: int | float, base_currency: str, target_currency: str) -> int | float:
        """
        Converts the price to target currency.
        :param price: price to convert
        :param base_currency: base currency to convert from
        :param target_currency: target currency to convert to
        :return: result of conversion
        """
        if target_currency.upper() not in CURRENCY_RATES:
            raise ValueError('Target currency must be in currency rates')
        base_price = price * CURRENCY_RATES[base_currency.upper()]
        return base_price / CURRENCY_RATES[target_currency.upper()]


class PriceDescriptor:
    """Price descriptor class"""

    def __get__(self, instance, owner):
        """Getter"""
        return instance.__dict__['price']

    def __set__(self, instance, value):
        """Setter"""
        if not isinstance(value, int | float):
            raise ValueError("Value must be numeric")
        if value < 0:
            raise ValueError("Value must be positive")
        instance.__dict__['price'] = value


class ProductWithDescriptor:
    """Product with descriptor class"""

    price = PriceDescriptor()
    currency = CurrencyDescriptor()

    def __init__(self, name: str, price: int | float, currency: str = 'UAH') -> None:
        """
        Constuctor
        :param name: name of the product
        :param price: price of the product
        :param currency: currency of the product
        """
        self.name = name
        self.price = price
        self.currency = currency

    def __str__(self) -> str:
        """String representation of the product"""
        return f"{self.name} {self.price} {self.currency}"

    def convert_currency(self, target_currency: str) -> int | float:
        """
        Converts the price to target currency.
        :param target_currency: tarrget currency to convert to
        :return: result of conversion
        """
        return CurrencyDescriptor().convert_currency(self.price, self.currency, target_currency)


if __name__ == "__main__":
    p1 = ProductWithDescriptor('P1', 400, currency='EUR')
    print(p1)
    print(p1.convert_currency('USD'))

    print(p1.convert_currency('UAH'))
