class MyClass:
    """
    Test Class
    """

    def __init__(self, value: str) -> None:
        """
        Constructor for Test Class
        :param value: test value
        """
        self.value = value

    def say_hello(self) -> str:
        """Method to return hello message"""
        return f"Hello, {self.value}"


def analyze_object(obj: object) -> None:
    """
    Function returns object type, attributes, and methods
    :param obj: object to be analyzed
    :return: String of object type, attributes, and methods
    """
    print(f"Object type: {type(obj)}")
    print(f"Attributes and methods: {dir(obj)}")

    for attr in dir(obj):
        attr_value = getattr(obj, attr)
        print(f"{attr}: {type(attr_value)}")


if __name__ == "__main__":
    objt = MyClass("World")
    analyze_object(objt)
