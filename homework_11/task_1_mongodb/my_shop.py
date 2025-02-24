"""
Module: data_initializer
------------------------
This script initializes and manages product and order data using MongoDB.
"""

from datetime import datetime

from order_repo import OrderRepository
from product_repo import ProductRepository

products = ProductRepository()
orders = OrderRepository()

products_list = [
    {
        "name": "Whiskas",
        "price": 10,
        "category": "Cat Food",
        "quantity": 100
    },
    {
        "name": "Pedigree",
        "price": 14,
        "category": "Dog Food",
        "quantity": 50
    },
    {
        "name": "Friskies",
        "price": 9,
        "category": "Cat Food",
        "quantity": 8
    },
    {
        "name": "Felix",
        "price": 8,
        "category": "Cat Food",
        "quantity": 45
    }
]

orders_list = [
    {
        "order_number": "ON_001",
        "client": "Frank Drebin",
        "products": [
            {
                "name": "Whiskas",
                "quantity": 10,
                "price": 10
            },
            {
                "name": "Friskies",
                "quantity": 4,
                "price": 9
            }
        ],
        "total": 136,
        "date": datetime.now()
    },
    {
        "order_number": "ON_002",
        "client": "Homer Simpson",
        "products": [
            {
                "name": "Whiskas",
                "quantity": 10,
                "price": 10
            },
            {
                "name": "Felix",
                "quantity": 5,
                "price": 8
            }
        ],
        "total": 140,
        "date": datetime.now()
    },
    {
        "order_number": "ON_003",
        "client": "Homer Simpson",
        "products": [
            {
                "name": "Whiskas",
                "quantity": 5,
                "price": 10
            }
        ],
        "total": 50,
        "date": datetime.now()
    },
]

if __name__ == "__main__":
    # products.insert_many(products_list)
    # orders.insert_many(orders_list)
    #
    # products.create_index()

    # products.update_stock("Felix", 0)
    products.delete_out_of_stock()
    print(orders.get_recent_orders())
    print(orders.get_sales_info())
    print(orders.get_total_order_amount_by_client("Homer Simpson"))
