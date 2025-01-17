# Initialize the expenses list
expenses = []

while True:
    print("\nExpense Tracker")
    print("1. Add a New Expense")
    print("2. Remove an Expense")
    print("3. View Total Expenses")
    print("4. Find Highest and Lowest Expense")
    print("5. List All Expenses")
    print("6. Exit")

    choice = int(input("Enter your choice (1-6): "))

    if choice == 1:
        # Add a new expense
        description = input("Enter the expense description: ")
        amount = float(input("Enter the expense amount: "))
        expenses.append((description, amount))
        print(f"Expense '{description}' of ${amount:.2f} added successfully.")

    elif choice == 2:
        # Remove an expense
        description = input("Enter the description of the expense to remove: ")
        found = False
        for i, (desc, amount) in enumerate(expenses):
            if desc.lower() == description.lower():
                expenses.pop(i)
                print(f"Expense '{description}' removed successfully.")
                found = True
                break
        if not found:
            print("Expense not found.")

    elif choice == 3:
        # View total expenses
        total = sum(amount for _, amount in expenses)
        print(f"Total expenses: ${total:.2f}")

    elif choice == 4:
        # Find highest and lowest expense
        if expenses:
            amounts = [amount for _, amount in expenses]
            print(f"Highest expense: ${max(amounts):.2f}")
            print(f"Lowest expense: ${min(amounts):.2f}")
        else:
            print("No expenses recorded yet.")

    elif choice == 5:
        # List all expenses
        if expenses:
            print("\nAll Expenses:")
            for desc, amount in expenses:
                print(f"{desc}: ${amount:.2f}")
        else:
            print("No expenses to display.")

    elif choice == 6:
        # Exit the program
        print("Exiting the Expense Tracker. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")


# Features
# Add Expenses: Add a new expense with a description and amount.
# Remove Expenses: Remove an expense by its description.
# View Totals: Show the total amount of all expenses.
# Highest/Lowest Expense: Identify the most and least expensive items.
# List Expenses: Display all expenses in a readable format.

# Concepts Applied
# Arrays: Store and manage a list of expenses.
# Conditionals: Handle user choices and error conditions.
# Loops: Iterate through the expense list.
# Math Operations: Calculate totals, highest, and lowest amounts.
# Strings: Manage expense descriptions and user input.