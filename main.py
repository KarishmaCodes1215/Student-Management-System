

import sqlite3

# Connect to the database
conn = sqlite3.connect("students.db")
cursor = conn.cursor()

# Create the table if it does not exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    student_id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    age TEXT,
    course TEXT
)
""")
conn.commit()

while True:
    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        student_id = input("Enter Student ID: ")
        name = input("Enter Student Name: ")
        age = input("Enter Student Age: ")
        course = input("Enter Course: ")

        try:
            cursor.execute(
                "INSERT INTO students VALUES (?, ?, ?, ?)",
                (student_id, name, age, course)
            )
            conn.commit()
            print("Student added successfully!")

        except sqlite3.IntegrityError:
            print("Student ID already exists!")

    elif choice == "2":
        cursor.execute("SELECT * FROM students")
        students = cursor.fetchall()

        if len(students) == 0:
            print("No student records found.")
        else:
            for student in students:
                print(student)

    elif choice == "3":
        student_id = input("Enter Student ID: ")

        cursor.execute(
            "SELECT * FROM students WHERE student_id = ?",
            (student_id,)
        )
        student = cursor.fetchone()

        if student:
            print(student)
        else:
            print("Student not found.")

    elif choice == "4":
        student_id = input("Enter Student ID: ")

        cursor.execute(
            "DELETE FROM students WHERE student_id = ?",
            (student_id,)
        )
        conn.commit()

        if cursor.rowcount > 0:
            print("Student deleted successfully!")
        else:
            print("Student not found.")

    elif choice == "5":
        print("Thank you!")
        break

    else:
        print("Invalid choice. Try again.")

conn.close()
