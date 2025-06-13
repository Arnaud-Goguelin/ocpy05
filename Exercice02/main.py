students = {
    "Alice": {"Math": 90, "French": 80, "History": 95},
    "Bob": {"Math": 75, "French": 85, "History": 70},
    "Charlie": {"Math": 88, "French": 92, "History": 78},
}


def choose_a_student() -> str:
    student = input("Please, choose a student:")
    if student.isdigit():
        raise ValueError("Input must be a name")
    if student not in students:
        raise ValueError(f"Student {student} doesn't exist in the list")
    return student


def display_grades(student: str) -> None:
    grades = students[student]
    print(f"{student}'s grades are:")
    for subject, grade in grades.items():
        print(f"{subject}: {grade}")
    return None


def calculate_average_grade(student: str) -> float:
    grades = students[student]
    total_grades = sum(grades.values())
    average_grade = total_grades / len(grades.values())
    return average_grade


def display_average_grade(student: str) -> None:
    average_grade = calculate_average_grade(student)
    print(f"Average grade for {student} is {average_grade}")
    return None


if __name__ == "__main__":
    try:
        student = choose_a_student()
        display_grades(student)
        display_average_grade(student)
    except ValueError as error:
        print("An error happened:")
        print(error)
