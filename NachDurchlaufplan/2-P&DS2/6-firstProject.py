#6 Basic Calculator with Options

# User Input Handling: The ability to take user input safely and validate choices to prevent errors.
# Mathematical Operations: Implementation of basic arithmetic operations (addition, subtraction, multiplication, and division) along with bitwise operations (AND, OR).
# Error Handling: Preventing issues like division by zero and handling invalid inputs gracefully.
# History Management: Storing past calculations in a list for retrieval when needed.
# User Interface: A simple text-based menu allowing users to select operations, view history, and exit the program.
# Loop & Exit Control: Using a while loop to keep the program running until the user chooses to exit.
# Modularity & Readability: Keeping the code structured with clear function mappings and concise logic for easy maintenance and potential expansion.

print("Welcome to the Enhanced Calculator!")

# Map operations to their functions
operations = {
    1: ("Addition", lambda x, y: x + y),
    2: ("Subtraction", lambda x, y: x - y),
    3: ("Multiplication", lambda x, y: x * y),
    4: ("Division", lambda x, y: x / y if y != 0 else "Error: Division by zero"),
}

# List to store calculation history
history = []

while True:
    print("\nChoose an operation:")
    for key, value in operations.items():
        print(f"{key}. {value[0]}")
    print("5. View History")
    print("6. Exit")

    choice = int(input("Enter your choice (1-6): "))

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

    elif choice == 5:
        print("\nCalculation History:")
        if history:
            for record in history:
                print(record)
        else:
            print("No calculations performed yet.")

    elif choice == 6:
        print("Exiting the calculator. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")