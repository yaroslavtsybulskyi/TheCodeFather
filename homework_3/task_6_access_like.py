import re


class User:
    """
    Class that creates a new instance of the User class.
    """

    __email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    def __init__(self, first_name, last_name, email):
        self._first_name = first_name
        self._last_name = last_name
        if not re.match(self.__email_regex, email):
            raise ValueError('Invalid email format')
        self._email = email

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value: str):
        self._first_name = value.strip()

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value: str):
        self._last_name = value.strip()

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value: str):
        if not re.match(self.__email_regex, value):
            raise ValueError("Invalid email format")
        self._email = value.strip()

    def __str__(self) -> str:
        """String representation of the User."""
        return f'First Name: {self._first_name} \nLast Name: {self._last_name} \nEmail: {self._email}'


if __name__ == '__main__':
    jim = User('Jim', 'Doe', 'jim@gmail.com')

    print(jim)
    jim.email = 'jim@yahoo.com'
    jim.first_name = "Jimothy"
    jim.last_name = "Mustard"
    print("***"*20)
    print(jim)
