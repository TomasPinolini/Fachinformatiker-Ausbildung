Personal Finance Manager
Overview
The Personal Finance Manager is a Python-based application that helps users track and categorize their financial transactions. It supports multiple categories, provides summary reports, and allows easy management of income and expenses.

Features
Category Management:
Categories include Food, Transport, Entertainment, Bills, and Other.
Ensures categories are initialized with dedicated CSV files.
Transaction Management:
Add transactions with descriptions, amounts, and type (income/expense).
View transactions by category or across all categories.
Summary Report:
Generates a financial summary, including total income, total expenses, and a breakdown by category.
Interactive Menu:
User-friendly menu for navigating the application.
File-Based Persistence:
Stores data in CSV files, ensuring all information is saved for future sessions.

Concepts Applied
File Handling:
Reads and writes to CSV files for transaction management.
JSON Configuration:
Uses a configuration file (config.json) to store category information.
Error Handling:
Manages invalid inputs and missing files gracefully.
Modular Programming:
Organized into functions for better readability and maintainability.
Data Processing:
Summarizes data across categories and calculates totals dynamically.
User Interaction:
Collects input from users to execute various operations.