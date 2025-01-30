class UnknownOperatorException(Exception):
    """
    Custom exception raised when an unknown operator is encountered.
    """

    def __init__(self, operator: str) -> None:
        """
        Constructor.
        :param operator: Operator to check.
        """
        message = f'Unknown operator "{operator}"'
        super().__init__(message)


def calculator():
    """
    Calculator function which supports 4 operations.
    """
    try:
        first_number = float(input("Enter first number: "))
        second_number = float(input("Enter second number: "))
        operator = input("Enter operator (+, -, *, /): ")

        if operator == "+":
            result = first_number + second_number
        elif operator == "-":
            result = first_number - second_number
        elif operator == "*":
            result = first_number * second_number
        elif operator == "/":
            if second_number == 0:
                raise ZeroDivisionError("Cannot divide by zero")
            result = first_number / second_number
        else:
            raise UnknownOperatorException(operator)

        print(f"Result: {result}")

    except (ZeroDivisionError, ValueError, UnknownOperatorException, OverflowError) as e:
        print(e)
    except KeyboardInterrupt:
        print("\nGoodbye!")


if __name__ == "__main__":
    calculator()
