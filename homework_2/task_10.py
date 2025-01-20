class SingletonMeta(type):
    """
    Singleton metaclass
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Method that calls the singleton instance
        :param args: arguments
        :param kwargs:  keyword arguments
        :return: return the singleton instance
        """
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonMeta, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):
    """
    Singleton class
    """

    def __init__(self):
        print("Creating instance")


if __name__ == "__main__":
    obj1 = Singleton()  # Creating instance
    obj2 = Singleton()
    obj3 = Singleton()
    print(obj1 is obj2)  # True
    print(obj1 is obj3)
