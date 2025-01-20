from typing import Any


class Calculator:
    """Test Class"""

    def add(self, a: int, b: int) -> int:
        """
        Function to add two numbers
        :param a: first number
        :param b: second number
        :return: sum of two numbers
        """
        return a + b

    def subtract(self, a: int, b: int) -> int:
        """
        Function to subtract two numbers
        :param a: The number to subtract from
        :param b: The number to subtract
        :return: difference of two numbers
        """
        return a - b


def call_function(obj: object, method_name: str, *args: Any) -> Any:
    """
    Function that dynamically calls the object method
    :param obj: object to be used
    :param method_name: method name to be called
    :param args: arguments to be passed
    :return: the result of calling method
    """
    if not hasattr(obj, method_name):
        raise AttributeError(f"{obj} does not have such method: {method_name}")

    method = getattr(obj, method_name)

    if not callable(getattr(obj, method_name)):
        raise AttributeError(f"{method_name} is not callable")

    result = method(*args)

    return result


if __name__ == "__main__":
    calc = Calculator()
    print(call_function(calc, "add", 10, 5))  # 15
    print(call_function(calc, "subtract", 10, 5))  # 5
