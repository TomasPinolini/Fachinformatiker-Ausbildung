#7.1 Division by Zero.
try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    result = numerator / denominator
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Please enter valid numbers.")


#7.2 File Not Found.
try:
    file_name = input("Enter the name of the file to open: ")
    with open(file_name, "r") as file:
        content = file.read()
        print("File content:\n", content)
except FileNotFoundError:
    print("Error: The file does not exist.")


#7.3 Index Out of Range.
numbers = [10, 20, 30, 40, 50]

try:
    index = int(input("Enter the index to access (0-4): "))
    print("Element at index", index, "is:", numbers[index])
except IndexError:
    print("Error: Index out of range.")
except ValueError:
    print("Error: Please enter a valid integer.")


#7.4 Handle Multiple Exceptions.
try:
    value = int(input("Enter a number: "))
    result = 100 / value
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Division by zero.")
except ValueError:
    print("Error: Invalid input. Please enter a number.")
except Exception as e:
    print("An unexpected error occurred:", e)


#7.5 Custom Exception for Age Validation.
class AgeTooLowError(Exception):
    pass

try:
    age = int(input("Enter your age: "))
    if age < 18:
        raise AgeTooLowError("You must be at least 18 years old.")
    print("Access granted.")
except AgeTooLowError as e:
    print("Error:", e)
except ValueError:
    print("Error: Invalid input. Please enter a number.")