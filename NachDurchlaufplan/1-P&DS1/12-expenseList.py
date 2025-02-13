# Initialize the expenses list
expenses = []

while True:
    print("\nExpense Tracker")
    print("1. Add a New Expense")
    print("2. Remove an Expense")
    print("3. View Total Expenses")
    print("4. Find Highest and Lowest Expense")
    print("5. List All Expenses")
    print("6. Categorize Expenses")
    print("7. Export Expenses to a File")
    print("8. Exit")

    choice = int(input("Enter your choice (1-8): "))

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
        # Categorize expenses
        categories = {}
        for desc, amount in expenses:
            category = input(f"Enter a category for the expense '{desc}': ")
            if category in categories:
                categories[category] += amount
            else:
                categories[category] = amount
        print("\nExpenses by Category:")
        for category, total in categories.items():
            print(f"{category}: ${total:.2f}")

    elif choice == 7:
        # Export expenses to a file
        with open("expenses.txt", "w") as file:
            for desc, amount in expenses:
                file.write(f"{desc}: ${amount:.2f}\n")
        print("Expenses have been saved to 'expenses.txt'.")

    elif choice == 8:
        # Exit the program
        print("Exiting the Expense Tracker. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")

