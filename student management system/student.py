class Student:
    def __init__(self, name, roll, course):
        self.name = name
        self.roll = roll
        self.course = course

    def __str__(self):
        return f"{self.roll},{self.name},{self.course}"


def add_student():
    name = input("Name: ")
    roll = input("Roll No: ")
    course = input("Course: ")

    student = Student(name, roll, course)

    with open("students.txt", "a") as file:
        file.write(str(student) + "\n")

    print("Student added successfully!")


def view_students():
    try:
        with open("students.txt", "r") as file:
            print("\n--- Student List ---")
            for line in file:
                roll, name, course = line.strip().split(",")
                print(f"Roll: {roll}, Name: {name}, Course: {course}")
    except FileNotFoundError:
        print("No students found.")


while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        break
    else:
        print("Invalid choice!")