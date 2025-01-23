# Personal Finance Manager Project Plan
# Objective: Build a Personal Finance Manager that allows users to 
# track their income and expenses, categorize them into separate 
# files, and view data in meaningful ways.

import os
import csv
import json
from datetime import datetime

CATEGORY_DIR = "NachDurchlaufplan/2-P&DS2/13-FinalPyProject/categories"
CONFIG_FILE = "NachDurchlaufplan/2-P&DS2/13-FinalPyProject/config.json"

def initialize_categories():
    """Ensure the category directory and default categories exist."""
    if not os.path.exists(CATEGORY_DIR):
        os.makedirs(CATEGORY_DIR)
    if not os.path.exists(CONFIG_FILE):
        default_config = {
            "categories": ["Food", "Transport", "Entertainment", "Bills", "Other"]
        }
        with open(CONFIG_FILE, "w") as f:
            json.dump(default_config, f)

    with open(CONFIG_FILE, "r") as f:
        categories = json.load(f).get("categories", [])
    for category in categories:
        category_file = os.path.join(CATEGORY_DIR, f"{category}.csv")
        if not os.path.exists(category_file):
            with open(category_file, "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["Date", "Description", "Amount", "Type"])  # Add headers

def list_categories():
    """Display all available categories."""
    with open(CONFIG_FILE, "r") as f:
        categories = json.load(f).get("categories", [])
    if categories:
        print("Available categories:")
        for category in categories:
            print(f"- {category}")
    else:
        print("No categories available. Please add a category first.")

def add_transaction():
    """Add a new transaction with category selection."""
    with open(CONFIG_FILE, "r") as f:
        categories = json.load(f).get("categories", [])
    
    if not categories:
        print("No categories available. Please add a category first.")
        return
    
    # Show available categories with labels
    print("Select a category:")
    for idx, category in enumerate(categories, start=1):
        print(f"{idx}. {category}")
    
    try:
        category_choice = int(input("Enter the number corresponding to the category: "))
        if category_choice < 1 or category_choice > len(categories):
            print("Invalid choice. Please try again.")
            return
    except ValueError:
        print("Invalid input. Please enter a number.")
        return
    
    # Get the category name based on the user's choice
    category = categories[category_choice - 1]
    
    description = input("Enter the description: ")
    amount = float(input("Enter the amount: "))
    transaction_type = input("Enter type (income/expense): ").lower()

    file_path = os.path.join(CATEGORY_DIR, f"{category}.csv")
    with open(file_path, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([datetime.now().strftime("%Y-%m-%d"), description, amount, transaction_type])
    print(f"Transaction added to '{category}' successfully!")


def view_transactions():
    """View transactions with category selection."""
    with open(CONFIG_FILE, "r") as f:
        categories = json.load(f).get("categories", [])
    
    if not categories:
        print("No categories available. Please add a category first.")
        return
    
    print("Select a category:")
    for idx, category in enumerate(categories, start=1):
        print(f"{idx}. {category}")
    print("0. View all categories")
    
    try:
        category_choice = int(input("Enter the number corresponding to the category (or 0 for all): "))
        if category_choice < 0 or category_choice > len(categories):
            print("Invalid choice. Please try again.")
            return
    except ValueError:
        print("Invalid input. Please enter a number.")
        return
    
    if category_choice == 0:
        # View all categories
        print("Transactions across all categories:")
        for file_name in os.listdir(CATEGORY_DIR):
            print(f"\nCategory: {file_name.split('.')[0]}")
            with open(os.path.join(CATEGORY_DIR, file_name), "r") as file:
                reader = csv.reader(file)
                for row in reader:
                    print(row)
    else:
        # View transactions for the selected category
        category = categories[category_choice - 1]
        file_path = os.path.join(CATEGORY_DIR, f"{category}.csv")
        if not os.path.exists(file_path):
            print(f"No transactions found for category '{category}'.")
            return
        print(f"Transactions for {category}:")
        with open(file_path, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)

def generate_summary():
    """Generate and display a financial summary across all categories."""
    total_income = 0
    total_expense = 0
    category_totals = {}

    for file_name in os.listdir(CATEGORY_DIR):
        category = file_name.split('.')[0]
        category_income = 0
        category_expense = 0

        with open(os.path.join(CATEGORY_DIR, file_name), "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                amount = float(row["Amount"])
                if row["Type"].lower() == "income":
                    category_income += amount
                elif row["Type"].lower() == "expense":
                    category_expense += amount

        category_totals[category] = {
            "income": category_income,
            "expense": category_expense
        }
        total_income += category_income
        total_expense += category_expense

    print("\nFinancial Summary:")
    print(f"Total Income: ${total_income:.2f}")
    print(f"Total Expense: ${total_expense:.2f}")
    print(f"Net Balance: ${total_income - total_expense:.2f}\n")

    print("Breakdown by Category:")
    for category, totals in category_totals.items():
        print(f"{category}: Income = ${totals['income']:.2f}, Expense = ${totals['expense']:.2f}")

def main_menu():
    """Main menu for the finance manager."""
    initialize_categories()
    while True:
        print("\nPersonal Finance Manager")
        print("1. Add Transaction")
        print("2. View Transactions")
        print("3. Generate Summary")
        print("4. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            add_transaction()
        elif choice == "2":
            view_transactions()
        elif choice == "3":
            generate_summary()
        elif choice == "4":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main_menu()