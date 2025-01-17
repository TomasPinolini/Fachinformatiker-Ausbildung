#2.1 Simple Function to Greet a User.
def greet_user():
    name = input("Enter your name: ")
    print("Hello,", name + "!")

greet_user()


#2.2 Function to Add Two Numbers.
def add_numbers(a, b):
    return a + b

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
result = add_numbers(num1, num2)
print("The sum is:", result)


#2.3 Function to Find the Maximum of Two Numbers.
def find_max(a, b):
    if a > b:
        return a
    else:
        return b

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
print("The larger number is:", find_max(num1, num2))


#2.4 Function to Calculate the Factorial of a Number.
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

num = int(input("Enter a number: "))
print("The factorial of", num, "is:", factorial(num))


#2.5 Function to Check if a Number is Prime.
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

num = int(input("Enter a number: "))
if is_prime(num):
    print(num, "is a prime number.")
else:
    print(num, "is not a prime number.")


#2.6 Function to Reverse a String.
def reverse_string(s):
    return s[::-1]

text = input("Enter a string: ")
print("The reversed string is:", reverse_string(text))