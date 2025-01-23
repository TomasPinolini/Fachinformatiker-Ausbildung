#6.1 Check If a Number is Positive or Negative
num = float(input("Enter a number: "))
if num > 0:
    print("The number is positive.")
else:
    print("The number is negative or zero.")


#6.2 Even or Odd
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")


#6.3 Age Checker
age = int(input("Enter your age: "))
if age < 13:
    print("You are a child.")
elif age < 20:
    print("You are a teenager.")
else:
    print("You are an adult.")


#6.4 Find the Largest of Two Numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if num1 > num2:
    print("The larger number is:", num1)
elif num1 < num2:
    print("The larger number is:", num2)
else:
    print("Both numbers are equal.")


#6.5 Simple Grading System
score = int(input("Enter your score (0-100): "))

if score >= 90:
    print("You got an A!")
elif score >= 80:
    print("You got a B.")
elif score >= 70:
    print("You got a C.")
elif score >= 60:
    print("You got a D.")
else:
    print("You got an F.")


#6.6 Check If a Number is Divisible by 3 or 5
num = int(input("Enter a number: "))
if num % 3 == 0 or num % 5 == 0:
    print("The number is divisible by 3 or 5.")
else:
    print("The number is not divisible by 3 or 5.")
    

#6.7 Check the Grade Range
grade = int(input("Enter your grade (0-100): "))
if 90 <= grade <= 100:
    print("Excellent!")
elif 75 <= grade < 90:
    print("Good job.")
elif 50 <= grade < 75:
    print("Needs improvement.")
else:
    print("Failing grade.")