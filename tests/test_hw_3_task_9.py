import pytest

from homework_3.task_9_comparison import *


def test_product_with_get_set_price_value_error():
    with pytest.raises(ValueError):
        product = ProductWithGetSet('book', 5)
        product.set_price(-4)


def test_product_with_properties_price_value_error():
    with pytest.raises(ValueError):
        product = ProductWithProperty('book', 5)
        product.price = -4


def test_product_with_description_price_value_error():
    with pytest.raises(ValueError):
        product = ProductWithDescriptor('book', 5)
        product.price = -4
