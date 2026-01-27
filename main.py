# Student Management System using Python (File Handling + OOP)

class Student:
    def __init__(self, roll, name, marks):
        self.roll = roll
        self.name = name
        self.marks = marks

    def __str__(self):
        return f"{self.roll},{self.name},{self.marks}"


FILE_NAME = "students.txt"


def add_student():
    roll = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    marks = input("Enter Marks: ")

    student = Student(roll, name, marks)

    with open(FILE_NAME, "a") as file:
        file.write(str(student) + "\n")

    print("✅ Student added successfully!")


def view_students():
    try:
        with open(FILE_NAME, "r") as file:
            students = file.readlines()
            if not students:
                print("⚠ No records found.")
            else:
                print("\n--- Student Records ---")
                for student in students:
                    roll, name, marks = student.strip().split(",")
                    print(f"Roll: {roll}, Name: {name}, Marks: {marks}")
    except FileNotFoundError:
        print("⚠ File not found.")


def search_student():
    roll_search = input("Enter Roll Number to Search: ")
    found = False

    with open(FILE_NAME, "r") as file:
        for student in file:
            roll, name, marks = student.strip().split(",")
            if roll == roll_search:
                print(f"🎯 Found → Roll: {roll}, Name: {name}, Marks: {marks}")
                found = True
                break

    if not found:
        print("❌ Student not found.")


def update_student():
    roll_update = input("Enter Roll Number to Update: ")
    updated = False
    students = []

    with open(FILE_NAME, "r") as file:
        students = file.readlines()

    with open(FILE_NAME, "w") as file:
        for student in students:
            roll, name, marks = student.strip().split(",")
            if roll == roll_update:
                name = input("Enter New Name: ")
                marks = input("Enter New Marks: ")
                file.write(f"{roll},{name},{marks}\n")
                updated = True
            else:
                file.write(student)

    if updated:
        print("✅ Student record updated.")
    else:
        print("❌ Student not found.")


def delete_student():
    roll_delete = input("Enter Roll Number to Delete: ")
    deleted = False
    students = []

    with open(FILE_NAME, "r") as file:
        students = file.readlines()

    with open(FILE_NAME, "w") as file:
        for student in students:
            roll, name, marks = student.strip().split(",")
            if roll == roll_delete:
                deleted = True
            else:
                file.write(student)

    if deleted:
        print("🗑 Student deleted successfully.")
    else:
        print("❌ Student not found.")


def main():
    while True:
        print("\n===== Student Management System =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            print("👋 Exiting program. Thank you!")
            break
        else:
            print("⚠ Invalid choice. Try again.")


if __name__ == "__main__":
    main()
