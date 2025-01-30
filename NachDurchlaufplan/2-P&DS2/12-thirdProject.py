#9 Basic Calculator Project
print("Welcome to the Calculator!")

while True:
    print("\nSelect an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    try:
        choice = int(input("Enter your choice (1-5): "))

        if choice == 5:
            print("Exiting the calculator. Goodbye!")
            break  # Exit the loop

        if choice < 1 or choice > 5:
            print("Invalid choice. Please choose a valid option.")
            continue  # Skip to the next iteration of the loop

        # Take inputs for the operation
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        if choice == 1:
            print("Result:", num1 + num2)
        elif choice == 2:
            print("Result:", num1 - num2)
        elif choice == 3:
            print("Result:", num1 * num2)
        elif choice == 4:
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
            else:
                print("Result:", num1 / num2)

    except ValueError:
        print("Error: Please enter a valid number.")

<<<<<<< HEAD



=======
# Features
# Basic Arithmetic Operations:
# Supports addition, subtraction, multiplication, and division.
# Division by Zero Handling:
# Provides error handling for cases where the divisor is zero.
# Input Validation:
# Detects invalid numeric inputs and prompts the user to enter valid numbers.
# Dynamic Menu:
# Interactive menu to allow users to select operations or exit the calculator.
# Graceful Exit:
# Cleanly exits the program when the user selects the "Exit" option.
# Error Messaging:
# Informs users of invalid menu choices or incorrect inputs, ensuring a smooth experience.

# Concepts Applied
# Conditionals:
# Used extensively for menu navigation, operation selection, and error handling.
# Loops:
# Implements a continuous loop for repeated calculations until the user chooses to exit.
# Functions:
# Operations (addition, subtraction, etc.) are implemented in separate conditional blocks, emphasizing modularity.
# Error Handling:
# Catches ValueError exceptions to manage invalid numeric inputs.
# User Interaction:
# Prompts users for input at every step, ensuring dynamic and personalized interactions.
>>>>>>> 24e39dae881d2a8ddfea838b6b80ca5293a3a5e4
