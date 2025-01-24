class Person:
    """
    Class representing a person
    """

    def __init__(self, name: str, age: int):
        """
        Person constructor
        :param name: name of the person
        :param age: age
        """
        self.name = name
        self.age = age

    def __lt__(self, other) -> bool:
        """Method for comparing two objects, less than"""
        if isinstance(other, Person):
            return self.age < other.age
        return NotImplemented

    def __gt__(self, other) -> bool:
        """Method for comparing two objects, greater than"""
        if isinstance(other, Person):
            return self.age > other.age
        return NotImplemented

    def __eq__(self, other) -> bool:
        """Method for comparing two objects, equal"""
        if isinstance(other, Person):
            return self.age == other.age
        return NotImplemented

    def __repr__(self) -> str:
        """String representation of the person"""
        return f'Person(name={self.name}, age={self.age})'


if __name__ == '__main__':
    persons = [Person('Alice', 45), Person('Bob', 20), Person('Charlie', 20),
               Person('Dave', 10)]

    print(f"ASC sorting: {sorted(persons)}")
    print(f"DESC sorting: {sorted(persons, reverse=True)}")

    print(f"Check equal method. Bob and Charlie are equal: {persons[1] == persons[2]}")
    print(f"Check equal method. Alice and Bob are equal: {persons[0] == persons[1]}")
