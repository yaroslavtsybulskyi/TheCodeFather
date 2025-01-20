import inspect


class Parent:
    """
    test class representing parent
    """

    def parent_method(self):
        """test method for parent class"""
        pass


class Child(Parent):
    """
    test class representing child
    """

    def child_method(self):
        """test method for child class"""
        pass


def analyze_inheritance(cls) -> None:
    """
    Function to analyze inheritance methods
    :param cls: class to analyze
    """
    print(f"Analyzing inheritance for {cls.__name__}")
    inherited_methods = {}

    for base_class in cls.__bases__:
        for name, method in inspect.getmembers(base_class, predicate=inspect.isfunction):
            if name not in cls.__dict__:
                inherited_methods[name] = base_class.__name__

    if inherited_methods:
        print("Inherited methods:")
        for method, origin in inherited_methods.items():
            print(f"{method} is inherited from {origin}")
    else:
        print("No inherited methods")


if __name__ == '__main__':
    analyze_inheritance(Child)
