# 12 Basic Calculator with Options.

print("Welcome to the Basic Calculator!")

while True:
    print("\nChoose an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Bitwise AND")
    print("6. Bitwise OR")
    print("7. Exit")

    choice = int(input("Enter your choice (1-7): "))

    if choice in [1, 2, 3, 4, 5, 6]:
        # Get two numbers from the user
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))

        # Perform the chosen operation
        if choice == 1:
            result = num1 + num2
            print("The result of addition is:", result)
        elif choice == 2:
            result = num1 - num2
            print("The result of subtraction is:", result)
        elif choice == 3:
            result = num1 * num2
            print("The result of multiplication is:", result)
        elif choice == 4:
            if num2 != 0:
                result = num1 / num2
                print("The result of division is:", result)
            else:
                print("Error: Division by zero is not allowed.")
        elif choice == 5:
            result = num1 & num2
            print("The result of bitwise AND is:", result)
        elif choice == 6:
            result = num1 | num2
            print("The result of bitwise OR is:", result)

    elif choice == 7:
        print("Exiting the calculator. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")