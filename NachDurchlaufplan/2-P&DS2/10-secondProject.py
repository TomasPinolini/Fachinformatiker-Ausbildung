#7 Student Grade Management System.
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


# Features
# File-Based Persistence:
# Stores student records in a CSV file to maintain data across sessions.
# View All Students:
# Displays all student names and grades in a user-friendly format.
# Add a New Student:
# Allows adding a new student record with a name and grade.
# Update a Student's Grade:
# Finds a specific student by name and updates their grade.
# Delete a Student Record:
# Removes a student record by matching the name.
# Interactive Menu:
# Provides a dynamic menu for users to navigate system features easily.
# Error Handling:
# Manages cases where the file is missing or a record is not found.

# Concepts Applied
# File Handling:
# Reads from and writes to a CSV file using Python's csv module.
# Ensures the file is created if it doesn't already exist.
# Functions:
# Modular design with separate functions for viewing, adding, updating, and deleting records.
# Loops:
# Implements a main menu loop to keep the system running until the user exits.
# Conditionals:
# Validates user input and directs the flow to the corresponding system feature.
# Data Structures:
# Processes and manipulates student data stored in a list format from the CSV file.
# User Interaction:
# Collects user input for all operations, providing feedback for each action.