def calculate_average(numbers_list: list[int | float]) -> float:
    """
    Calculates the average of a list of numbers.

    Args:
        numbers_list: A list of integers or floats whose average needs to be
            calculated.

    Returns:
        A float representing the average of the numbers in the list.

    Raises:
        ValueError: If the list is empty.
        ValueError: If the list contains non-numeric values.
    """
    if any(not isinstance(item, (int, float)) for item in numbers_list):
        raise ValueError("The list contains non-numeric values")
    if len(numbers_list) == 0:
        raise ValueError("The list is empty")
    return sum(numbers_list) / len(numbers_list)


if __name__ == "__main__":
    try:
        # numbers = [10, 20, 30, 40, 50]
        # numbers = [30, 50, 80]
        # numbers = ["a", 50, 80]
        numbers = []
        average = calculate_average(numbers)
        print("Average is :", average)
    except ValueError as error:
        print("An error happened:")
        print(error)
