from xml.etree import ElementTree as ET


def get_product_data(filename: str) -> None:
    """
    Retrieves product data from an XML file and prints it.
    :param filename: The name of the XML file containing product data.
    :raises FileNotFoundError: If the file is not found.
    :raises Exception: For any other errors that occur during processing.
    """
    try:
        tree = ET.parse(filename)
        root = tree.getroot()

        for product in root.findall('product'):
            name = product.find('name').text
            quantity = product.find('quantity').text
            print(f'{name} {quantity}')
    except FileNotFoundError:
        print('File not found')
    except Exception as e:
        print(f"Error: {e}")


def update_product_quantity(filename: str, product_name: str, quantity: int) -> None:
    """
    Updates the quantity of a specified product in an XML file.
    :param filename: The name of the XML file to update.
    :param product_name: The name of the product to update.
    :param quantity: The new quantity of the product.
    :raises Exception: For any errors that occur during processing.
    """
    try:
        tree = ET.parse(filename)
        root = tree.getroot()

        product_found = False

        for product in root.findall('product'):
            if product.find('name').text == product_name:
                product.find('quantity').text = str(quantity)
                product_found = True
                break

        if product_found:
            tree.write(filename, encoding='utf-8', xml_declaration=True)
        else:
            print(f'Product {product_name} was not found in the list of products')
    except Exception as e:
        print(f"Error: {e}")


if __name__ == '__main__':
    get_product_data('data/products.xml')
    update_product_quantity('data/products.xml', 'Молоко', 150)
    get_product_data('data/products.xml')
