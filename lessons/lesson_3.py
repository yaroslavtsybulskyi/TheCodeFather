class NameDescriptor:
    def __get__(self, instance, owner):
        return instance.__dict__['name']

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise ValueError("Name should be a string")
        if not value.strip():
            raise ValueError("Person must have a name")
        instance.__dict__['name'] = value

    def __delete__(self, instance):
        raise AttributeError("Person's name cannot be deleted")


class EmailDescriptor:
    def __get__(self, instance, owner):
        return instance.__dict__['email']

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise ValueError("Email must be a string")
        if not value.strip():
            raise ValueError("Email should not be empty")
        instance.__dict__['email'] = value

    def __delete__(self, instance):
        raise AttributeError("Email cannot be deleted")


class AddressDescriptor:
    def __get__(self, instance, owner):
        return instance.__dict__['address']

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise ValueError("Address must be a string")
        if not value.strip():
            raise ValueError("Address should not be empty")
        instance.__dict__['address'] = value

    def __delete__(self, instance):
        raise AttributeError("Address cannot be deleted")


class Person:
    name = NameDescriptor()
    email = EmailDescriptor()
    address = AddressDescriptor()

    def __init__(self, name, email, address):
        self.name = name
        self.email = email
        self.address = address

    def __str__(self):
        return f"{self.name}: {self.email} {self.address}"


p1 = Person("James", "test@example.com", "Valid address")

print(p1)
