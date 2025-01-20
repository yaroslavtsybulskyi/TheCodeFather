from typing import Any


class MyClass:
    """
    My Class
    """

    def greet(self, name) -> str:
        """
        Function that returns the greeting
        :param name:  name of the person to greet.
        :return: greeting to the person.
        """
        return f"Hello, {name}!"


class Proxy:
    """
    Proxy class that takes object as an input and forwards method calls to this object and logs the calls
    """

    def __init__(self, obj) -> None:
        """
        Proxy class constructor
        :param obj: object to forward method calls.
        """
        self.obj = obj

    def __getattr__(self, name: str) -> Any:
        """
        Function that intercepts calls to this object and logs the calls
        :param name: name of the method call.
        :return: the result of the method call.
        """
        attr = getattr(self.obj, name)

        if callable(attr):
            def wrapper(*args):
                print(f"Calling method {name} with args {args}")
                return attr(*args)

            return wrapper
        return attr


if __name__ == "__main__":
    obj = MyClass()
    proxy = Proxy(obj)
    print(proxy.greet("Alice"))
