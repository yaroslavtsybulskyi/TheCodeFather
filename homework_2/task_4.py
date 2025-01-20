def create_class(class_name: str, methods: dict) -> type:
    """
    Method that dynamically creates a class from its name.
    :param class_name: class name
    :param methods: methods dictionary
    :return: dynamically created class
    """
    return type(class_name, (object,), methods)


def say_hello(self):
    """Greeting function"""
    return "Hello!"


def say_goodbye(self):
    """Goodbye function"""
    return "Goodbye!"


methods = {
    "say_hello": say_hello,
    "say_goodbye": say_goodbye
}


if __name__ == "__main__":
    MyDynamicClass = create_class("MyDynamicClass", methods)

    obj = MyDynamicClass()
    print(obj.say_hello())  # Hello!
    print(obj.say_goodbye())  # Goodbye!
