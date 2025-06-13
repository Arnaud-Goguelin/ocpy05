def choose_a_student(students: dict[str : dict[str:int]]) -> str:
    """
    Choose a student from a predefined list.

    This function asks the user to input the name of a student. It validates the
    input, ensuring that it is not a numeric value and that it corresponds to an
    existing student in the list. If these conditions are not met, appropriate
    errors are raised. The function then returns the name of the chosen student
    if valid.

    :raises ValueError: If the input is a digit.
    :raises ValueError: If the input does not exist in the list of students.
    :return: The name of the selected student.
    :rtype: str
    """
    student = input("Please, choose a student:")
    if student.isdigit():
        raise ValueError("Input must be a name")
    if student not in students:
        raise ValueError(f"Student {student} doesn't exist in the list")
    return student


def display_grades(student: str, students: dict[str : dict[str:int]]) -> None:
    grades = students[student]
    print(f"{student}'s grades are:")
    for subject, grade in grades.items():
        print(f"{subject}: {grade}")
    return None


def calculate_average_grade(student: str, students: dict[str : dict[str:int]]) -> float:
    grades = students[student]
    total_grades = sum(grades.values())
    average_grade = total_grades / len(grades.values())
    return average_grade


def display_average_grade(student: str, students: dict[str : dict[str:int]]) -> None:
    average_grade = calculate_average_grade(student, students)
    print(f"Average grade for {student} is {average_grade}")
    return None


if __name__ == "__main__":
    students = {
        "Alice": {"Math": 90, "French": 80, "History": 95},
        "Bob": {"Math": 75, "French": 85, "History": 70},
        "Charlie": {"Math": 88, "French": 92, "History": 78},
    }

    try:
        student = choose_a_student(students)
        display_grades(student, students)
        display_average_grade(student, students)
    except ValueError as error:
        print("An error happened:")
        print(error)
