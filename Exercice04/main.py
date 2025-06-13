class MyClass:
    """
    Represents a class for managing and displaying a full name.

    Attributes:
        full_name (str): Full name of the individual.
    """

    def __init__(self, full_name) -> None:
        self.full_name = full_name

    def display_name(self) -> None:
        print(f"Le nom complet est : {self.full_name}")


class OtherClass:
    """
    Represents a person with a first name and last name.

    Attributes:
        first_name (str): The first name of the person.
        last_name (str): The last name of the person.
    """

    def __init__(self, first_name: str, last_name: str) -> None:
        self.first_name = first_name
        self.last_name = last_name

    def display_name(self) -> None:
        print(f"Nom complet : {self.first_name} {self.last_name}")
