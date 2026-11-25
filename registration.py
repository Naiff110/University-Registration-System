def register_student(student_name, course):
    if not student_name or not course:
        return "Registration failed"

    return "Registration successful"


if __name__ == "__main__":
    print(register_student("Naif", "Software Engineering"))
