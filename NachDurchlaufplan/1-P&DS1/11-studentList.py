# Initialize the student list
students = []

while True:
    print("\nStudent Management System")
    print("1. Add a New Student")
    print("2. Calculate Average Grade")
    print("3. Find Highest and Lowest Grade")
    print("4. Search for a Student")
    print("5. List All Students")
    print("6. Edit a Student’s Grade")
    print("7. Sort Students by Grade")
    print("8. Exit")

    choice = int(input("Enter your choice (1-8): "))

    if choice == 1:
        # Add a new student
        name = input("Enter the student's name: ")
        grade = float(input("Enter the student's grade: "))
        students.append((name, grade))
        print(f"Student {name} added successfully.")

    elif choice == 2:
        # Calculate average grade
        if students:
            total = sum(grade for _, grade in students)
            average = total / len(students)
            print(f"The average grade of all students is: {average:.2f}")
        else:
            print("No students available to calculate the average.")

    elif choice == 3:
        # Find highest and lowest grades
        if students:
            grades = [grade for _, grade in students]
            print(f"Highest grade: {max(grades)}")
            print(f"Lowest grade: {min(grades)}")
        else:
            print("No students available to find grades.")

    elif choice == 4:
        # Search for a student
        search_name = input("Enter the name of the student to search for: ")
        found = False
        for name, grade in students:
            if name.lower() == search_name.lower():
                print(f"Student found: {name} with grade {grade}")
                found = True
                break
        if not found:
            print("Student not found.")

    elif choice == 5:
        # List all students
        if students:
            print("\nList of Students:")
            for name, grade in students:
                print(f"{name}: {grade}")
        else:
            print("No students in the system.")

    elif choice == 6:
        # Edit a student's grade
        edit_name = input("Enter the name of the student whose grade you want to edit: ")
        for i, (name, grade) in enumerate(students):
            if name.lower() == edit_name.lower():
                new_grade = float(input(f"Enter the new grade for {name}: "))
                students[i] = (name, new_grade)
                print(f"{name}'s grade updated successfully.")
                break
        else:
            print("Student not found.")

    elif choice == 7:
        # Sort students by grade
        if students:
            sorted_students = sorted(students, key=lambda x: x[1], reverse=True)
            print("Students sorted by grades:")
            for name, grade in sorted_students:
                print(f"{name}: {grade}")
        else:
            print("No students available to sort.")

    elif choice == 8:
        # Exit the program
        print("Exiting the system. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")


