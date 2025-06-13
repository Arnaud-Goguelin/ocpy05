def choose_a_student(students: dict[str : dict[str:int]]) -> str:
    """
    Choose a student from the predefined list.

    Args:
        students: Dictionary of student names and their grades

    Returns:
        Name of the selected student

    Raises:
        ValueError: If input is invalid or student not found

    """
    student = input("Please, choose a student:").strip()
    if student.isdigit():
        raise ValueError("Input must be a name")
    if student not in students:
        raise ValueError(f"Student {student} doesn't exist in the list")
    return student


def display_grades(student: str, students: dict[str : dict[str:int]]) -> None:
    """
    Displays in terminal the grades of a student in all their subjects.

    Args:
        student: The name of the student whose grades are to be displayed.
        students: A dictionary where the key is the student's name and the
            value is another dictionary mapping subjects to grade values.

    Returns:
        None
    """
    grades = students[student]
    print(f"{student}'s grades are:")
    for subject, grade in grades.items():
        print(f"{subject}: {grade}")
    return None


def calculate_average_grade(student: str, students: dict[str : dict[str:int]]) -> float:
    """
    Calculate the average grade for a specified student from a group of students.

    Args:
        student: The name of the student whose average grade is to be calculated.
        students: A dictionary where keys are student names and values are
            dictionaries. Each dictionary contains subject names as keys and their
            respective grades as values.

    Returns:
        The average grade of the specified student as a float.
    """
    grades = students[student]
    average_grade = sum(grades.values()) / len(grades.values())
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
