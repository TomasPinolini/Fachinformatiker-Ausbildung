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




