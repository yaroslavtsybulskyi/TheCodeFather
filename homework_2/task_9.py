class DynamicProperties:
    """
    Class DynamicProperties where it is possible to add properties dynamically.
    """

    def __init__(self):
        self._attributes = {}

    def add_property(self, property_name: str, property_value: str = 'default') -> None:
        """
        Method that adds a property to the class.
        :param property_name: the name of the property.
        :param property_value: value of the property.
        """
        self._attributes[property_name] = property_value

        def getter(self):
            return self._attributes[property_name]

        def setter(self, value):
            self._attributes[property_name] = value

        setattr(self, property_name, property(getter, setter).__get__(self))


if __name__ == '__main__':
    obj = DynamicProperties()
    obj.add_property('name', 'default_name')
    print(obj.name)  # default_name
    obj.name = "Python"
    print(obj.name)  # Python
