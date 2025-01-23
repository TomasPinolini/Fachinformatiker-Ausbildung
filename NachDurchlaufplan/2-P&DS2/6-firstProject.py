#6 Basic Calculator with Options

print("Welcome to the Enhanced Calculator!")

# Map operations to their functions
operations = {
    1: ("Addition", lambda x, y: x + y),
    2: ("Subtraction", lambda x, y: x - y),
    3: ("Multiplication", lambda x, y: x * y),
    4: ("Division", lambda x, y: x / y if y != 0 else "Error: Division by zero"),
    5: ("Bitwise AND", lambda x, y: x & y),
    6: ("Bitwise OR", lambda x, y: x | y)
}

# List to store calculation history
history = []

while True:
    print("\nChoose an operation:")
    for key, value in operations.items():
        print(f"{key}. {value[0]}")
    print("7. View History")
    print("8. Exit")

    choice = int(input("Enter your choice (1-8): "))

    if choice in operations:
        # Get two numbers from the user
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))

        # Perform the chosen operation
        operation_name, operation_func = operations[choice]
        result = operation_func(num1, num2)
        print(f"The result of {operation_name} is:", result)

        # Store the operation in history
        history.append(f"{operation_name} of {num1} and {num2} = {result}")

    elif choice == 7:
        print("\nCalculation History:")
        if history:
            for record in history:
                print(record)
        else:
            print("No calculations performed yet.")

    elif choice == 8:
        print("Exiting the calculator. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")


# Features
# Basic Arithmetic Operations:
# Includes addition, subtraction, multiplication, and division.
# Handles division by zero gracefully.
# Bitwise Operations:
# Supports bitwise AND and OR for integer inputs.
# Calculation History:
# Tracks past calculations and allows users to view them during the session.
# Dynamic Menu:
# Provides an interactive menu with options for operations, viewing history, and exiting the program.
# Input Validation:
# Detects invalid choices and prompts the user to try again.
# Extensible Structure:
# Uses a dictionary to map operation numbers to functions, making it easy to add new operations in the future.

# Concepts Applied
# Functions:
# Uses lambda functions to perform calculations dynamically based on user choice.
# Loops:
# Implements a continuous loop to allow multiple operations until the user chooses to exit.
# Conditionals:
# Validates user input and handles different menu options.
# Data Structures:
# Stores calculation history in a list and operations in a dictionary for efficient access.
# Error Handling:
# Checks for division by zero and displays an appropriate error message.
# User Interaction:
# Collects user input for operation choice and operands, providing feedback for all actions.
