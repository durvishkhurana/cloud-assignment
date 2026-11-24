import sys


def calculate_percentage(marks):
    if not marks:
        raise ValueError("enter at least one mark")
    if any(not 0 <= mark <= 100 for mark in marks):
        raise ValueError("marks must be between 0 and 100")
    return sum(marks) / len(marks)


def calculate_grade(percentage):
    if percentage >= 80:
        return "A (10 points)"
    if percentage >= 60:
        return "B (8 points)"
    if percentage >= 40:
        return "C (6 points)"
    return "F (0 points)"


def main():
    try:
        percentage = calculate_percentage([float(arg) for arg in sys.argv[1:]])
    except ValueError as error:
        sys.exit(f"Error: {error}")
    print(f"Percentage: {percentage:.2f}")
    print(f"Grade: {calculate_grade(percentage)}")


if __name__ == "__main__":
    main()
