class LimitedAttributesMeta(type):
    """
    Metaclass which limits the number of the attributes to a certain value.
    """

    max_attributes = 3

    def __init__(cls, name, bases, attrs):
        not_magic_attributes = [key for key in attrs if not key.startswith('_')]
        if len(not_magic_attributes) > cls.max_attributes:
            raise TypeError(f"Class {name} can not have more than {cls.max_attributes} attributes.")


class LimitedClass(metaclass=LimitedAttributesMeta):
    """
    Class for testing metaclass above
    """
    attr1 = 1
    attr2 = 2
    attr3 = 3
    attr4 = 4  # Викличе помилку


obj = LimitedClass()
