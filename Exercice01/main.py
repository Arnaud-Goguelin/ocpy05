def ask_for_name() -> str:
    """
    Asks the user for their name and validates the input.

    Raises:
        ValueError: If the input is empty.
        ValueError: If the input is a purely numeric string.

    Returns:
        str: The validated name provided by the user.
    """
    name = input("What is your name? ")
    if not name:
        raise ValueError("Input cannot be empty")
    if name.isdigit():
        raise ValueError("Input must be a string")
    return name


def ask_for_age() -> str:
    """
    Asks the user for their age and validates the input.

    Raises:
        ValueError: If the input is empty.
        ValueError: If the input is not numeric.

    Returns:
        str: The validated age provided by the user.
    """
    age = input("What is your age? ")
    if not age:
        raise ValueError("Input cannot be empty")
    if not age.isdigit():
        raise ValueError("Input must be a number")
    return age


def print_greetings(name: str, age: str) -> None:
    """
    Prints a personalized greeting message including the name and age of a person.

    Args:
        name (str): The name of the person to greet.
        age (str): The age of the person to include in the greeting.

    Returns:
        None
    """
    print(f"Hello, I'm {name} and I'm {age} years old.")
    return None


if __name__ == "__main__":
    try:
        name = ask_for_name()
        age = ask_for_age()
        print_greetings(name, age)
    except ValueError as error:
        print("An error happened:")
        print(error)
