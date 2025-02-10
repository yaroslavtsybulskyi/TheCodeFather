"""
Discount Calculator Module
This module provides a function to calculate the discounted price of a product.
"""


def calculate_discount(price: float, discount: float) -> float:
    """
    Returns the price of the product after discounting.
    :param price: price of the product before discount.
    :param discount: percentage of the discount.
    :return: price of the product after discount.

    :raises ValueError: if price is less than 0.
    :raises ValueError: if discount is not a number.
    :raises TypeError: if price is not a number.
    :raises TypeError: if discount is not a number.
    """
    if not isinstance(price, (float, int)):
        raise TypeError("Price must be a float")
    if not isinstance(discount, (float, int)):
        raise TypeError("Discount percentage must be a float")
    if price <= 0:
        raise ValueError("Price must be bigger than 0")
    if discount < 0:
        raise ValueError("Discount must be bigger than 0")
    if discount >= 100:
        return 0
    return round(price * (1 - discount / 100), 2)


if __name__ == "__main__":
    print(calculate_discount(100, 20))
    print(calculate_discount(50, 110))
    print(calculate_discount(150, 80))
