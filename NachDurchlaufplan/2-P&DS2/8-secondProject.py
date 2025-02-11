#7 Student Grade Management System.

# CSV File Management: Using Python’s csv module to store, retrieve, update, and delete student records persistently.
# Data Input and Validation: Ensuring user input is correctly formatted, preventing empty or incorrect data entries.
# CRUD Operations: Implementing the four core operations:
# Create: Add new student records.
# Read: View all student records.
# Update: Modify a student's grade.
# Delete: Remove a student record.
# Error Handling: Managing file-related exceptions and handling cases where records are missing.
# User Interface: A simple, menu-driven text-based interface that allows users to interact with the system.
# Persistence: Ensuring student data remains saved between program runs by storing it in a CSV file.
# Scalability & Maintainability: Writing modular and readable code that can be expanded to include more features like searching or grade statistics.

import csv

# File to store the student records
FILE_NAME = "students.csv"

# Ensure the file exists
try:
    with open(FILE_NAME, "x", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Grade"])  # Add header
except FileExistsError:
    pass

# Function to display all student records
def view_students():
    print("\nStudent Records:")
    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                print(", ".join(row))
    except FileNotFoundError:
        print("No records found!")

# Function to add a new student
def add_student():
    name = input("Enter the student's name: ")
    grade = input("Enter the student's grade: ")

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, grade])
    print(f"Record for {name} added successfully!")

# Function to update a student's grade
def update_student():
    name_to_update = input("Enter the name of the student to update: ")
    found = False
    rows = []

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row and row[0] == name_to_update:
                new_grade = input(f"Enter the new grade for {name_to_update}: ")
                row[1] = new_grade
                found = True
            rows.append(row)

    if found:
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(rows)
        print(f"Grade for {name_to_update} updated successfully!")
    else:
        print(f"No record found for {name_to_update}.")

# Function to delete a student record
def delete_student():
    name_to_delete = input("Enter the name of the student to delete: ")
    found = False
    rows = []

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row and row[0] == name_to_delete:
                found = True
                continue  # Skip this row
            rows.append(row)

    if found:
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(rows)
        print(f"Record for {name_to_delete} deleted successfully!")
    else:
        print(f"No record found for {name_to_delete}.")

# Main menu
while True:
    print("\nStudent Grade Management System")
    print("1. View all students")
    print("2. Add a new student")
    print("3. Update a student's grade")
    print("4. Delete a student record")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        view_students()
    elif choice == "2":
        add_student()
    elif choice == "3":
        update_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        print("Exiting the system. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")


