students = []

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

        student = {
            "ID": student_id,
            "Name": name,
            "Age": age,
            "Course": course
        }

        students.append(student)
        print("Student added successfully!")

    elif choice == "2":
        if len(students) == 0:
            print("No student records found.")
        else:
            for student in students:
                print(student)

    elif choice == "3":
        student_id = input("Enter Student ID: ")
        found = False

        for student in students:
            if student["ID"] == student_id:
                print(student)
                found = True
                break

        if not found:
            print("Student not found.")

    elif choice == "4":
        student_id = input("Enter Student ID: ")
        found = False

        for student in students:
            if student["ID"] == student_id:
                students.remove(student)
                print("Student deleted successfully!")
                found = True
                break

        if not found:
            print("Student not found.")

    elif choice == "5":
        print("Thank you!")
        break

    else:
        print("Invalid choice. Try again.")