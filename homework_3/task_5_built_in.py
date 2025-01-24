def custom_len(obj) -> int:
    """
    Custom object length function
    :param obj: object to find length
    :return: the length of the object
    """
    if hasattr(obj, '__iter__'):
        count: int = 0
        for _ in obj:
            count += 1
        return count
    else:
        raise TypeError("Object must be iterable")


def custom_sum(*args) -> int | float:
    """
    Custom sum function
    :param args: arguments to add together
    :return: sum of the arguments
    """
    if len(args) == 0:
        raise ValueError("There must be at least one argument")

    elif len(args) == 1:
        if hasattr(args[0], "__iter__") and not isinstance(args[0], (str, bytes)):
            total = 0
            for item in args[0]:
                if isinstance(item, (int, float)):
                    total += item
                else:
                    raise TypeError(f"Unsupported type {type(item)}")
            return total
        else:
            raise TypeError("Object must be iterable")
    else:
        total = 0
        for item in args:
            if isinstance(item, (int, float)):
                total += item
            else:
                raise TypeError(f"Unsupported type {type(item)}")

        return total


def custom_min(*args) -> int | float:
    """
    Custom function that finds minimum value
    :param args: list of arguments to find minimum
    :return: minimal value
    """
    if len(args) == 0:
        raise ValueError("There must be at least one argument")

    elif len(args) == 1:
        if hasattr(args[0], "__iter__") and not isinstance(args[0], (str, bytes)):
            minimal = args[0][0]
            for item in args[0]:
                if isinstance(item, (int, float)):
                    if item < minimal:
                        minimal = item
                else:
                    raise TypeError(f"Unsupported type {type(item)}")
            return minimal
        else:
            raise TypeError("Object must be iterable")
    else:
        minimal = args[0]
        for item in args:
            if isinstance(item, (int, float)):
                if item < minimal:
                    minimal = item
            else:
                raise TypeError(f"Unsupported type {type(item)}")
        return minimal
