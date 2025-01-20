from typing import Any


class MutableClass:
    """ Class that can dynamically set and remove attributes """

    def add_attribute(self, attribute_name: str, attribute_value: Any) -> None:
        """
        Function that adds a new attribute.
        :param attribute_name: The name of the attribute.
        :param attribute_value: Value of the attribute.
        """
        setattr(self, attribute_name, attribute_value)

    def remove_attribute(self, attribute_name: str) -> None:
        """
        Removes the attribute.
        :param attribute_name: The name of the attribute to be removed.
        """
        delattr(self, attribute_name)


if __name__ == '__main__':
    obj = MutableClass()
    obj.add_attribute("name", "Python")
    print(obj.name)  # Python

    obj.remove_attribute("name")
    print(obj.name)  # Виникне помилка, атрибут видалений
