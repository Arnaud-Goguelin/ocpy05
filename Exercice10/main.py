class Person:
    """
    Represents a person with a name and age.

    Attributes:
        name (str): The name of the person. Must be a non-empty string.
        age (int): The age of the person. Must be a non-negative integer.
    """

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = self.__validate_age(age)

    def __setattr__(self, name: str, value: str | int) -> None:
        """Intercepts attribute assignment for validation."""
        if name == "name":
            value = self.__validate_name(value)
        if name == "age":
            value = self.__validate_age(value)
        super().__setattr__(name, value)

    @staticmethod
    def __validate_age(age: int) -> int:
        """Validates that a given age is a non-negative integer."""
        if age < 0:
            raise ValueError("Age cannot be negative")
        if not isinstance(age, int):
            raise ValueError("Age must be an integer")
        return age

    @staticmethod
    def __validate_name(name: str) -> str:
        """Validates that a given name is a non-empty string."""
        if not isinstance(name, str):
            raise ValueError("Name must be a string")
        if not name:
            raise ValueError("Name cannot be empty")
        return name

    # exercise ask for a method, yet magic method do it perfectly
    def __str__(self) -> str:
        """Displays the name and age of the person."""
        return f"Name: {self.name}, Age: {self.age}"


class Employee(Person):

    def __init__(self, name: str, age: int, salary: float) -> None:
        super().__init__(name, age)
        self.salary = salary

    def __setattr__(self, name: str, value: str | int | float) -> None:
        """Intercepts attribute assignment for validation."""
        if name == "salary":
            value = self.__validate_salary(value)
        # __setattr__ is not in bloc if in order to delegate validation of others attributes to class Person
        super().__setattr__(name, value)

    @staticmethod
    def __validate_salary(salary: float) -> float:
        """Validates that a given salary is a non-negative float."""
        if salary < 0:
            raise ValueError("Salary cannot be negative")
        if not isinstance(salary, float):
            raise ValueError("Salary must be a float")
        return salary

    def __str__(self) -> str:
        """Returns a string representation of the employee."""
        return f"{super().__str__()}, Salary: {self.salary}"


if __name__ == "__main__":
    try:
        bob = Person("Bob", 33)
        print(bob.__str__())
        tom_employee = Employee("Tom", 37, 1000.00)
        print(tom_employee.__str__())
    except (ValueError, TypeError) as error:
        print("An error happened:")
        print(error)
