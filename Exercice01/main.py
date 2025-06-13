def ask_for_name():
    name = input("What is your name? ")
    if not name:
        raise ValueError("Input cannot be empty")
    if name.isdigit():
        raise ValueError("Input must be a string")
    return name

def ask_for_age():
    age = input("What is your age? ")
    if not age:
        raise ValueError("Input cannot be empty")
    if not age.isdigit():
        raise ValueError("Input must be a number")
    return age

def print_greetings(name: str, age: str):
    print(f"Hello, I'm {name} and I'm {age} years old.")

if __name__ == "__main__":
    try:
        name = ask_for_name()
        age = ask_for_age()
        print_greetings(name, age)
    except ValueError as error:
        print("An error happened:")
        print(error)
