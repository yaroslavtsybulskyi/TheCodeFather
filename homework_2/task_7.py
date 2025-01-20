def log_methods(cls):
    """
    Class decorator that wraps all callable methods with logging
    :param cls: that to decorate
    :return: the decorated class
    """

    for attr_name, attr_value in cls.__dict__.items():
        if callable(attr_value):
            def make_wrapper(method, name):
                def wrapper(self, *args, **kwargs):
                    print(f"Logging: {name} called with args:{args}")
                    return method(self, *args, **kwargs)

                return wrapper

            setattr(cls, attr_name, make_wrapper(attr_value, attr_name))
    return cls


@log_methods
class MyClass:
    """
    Class to be decorated
    """

    def add(self, a: int, b: int) -> int:
        """
        Returns the sum of the two numbers
        :param a: first number
        :param b: second number
        :return: sum of two numbers
        """
        return a + b

    def subtract(self, a: int, b: int) -> int:
        """
        Returns the difference of the two numbers
        :param a: The number to subtract from
        :param b: the number to subtract
        :return: the difference of the two numbers
        """
        return a - b


if __name__ == '__main__':
    obj = MyClass()
    obj.add(5, 3)  # Logging: add called with (5, 3)
    obj.subtract(5, 3)  # Logging: subtract called with (5, 3)
