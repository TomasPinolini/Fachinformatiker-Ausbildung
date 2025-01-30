#8.1 Check if a Number is in a Range.
num = int(input("Enter a number: "))
if num >= 10 and num <= 20:
    print("The number is in the range 10-20.")
else:
    print("The number is outside the range.")


#8.2 Check Eligibility for Discount.
age = int(input("Enter your age: "))
is_member = input("Are you a member? (yes/no): ").lower() == "yes"

if age < 18 or is_member:
    print("You are eligible for a discount.")
else:
    print("You are not eligible for a discount.")


#8.3 Validate a Password.
password = input("Enter your password: ")

if len(password) >= 8 and "@" in password and not password.islower():
    print("Password is valid.")
else:
    print("Password is invalid.")


#8.4 Check if a Triangle is Valid
side1 = float(input("Enter the first side of the triangle: "))
side2 = float(input("Enter the second side of the triangle: "))
side3 = float(input("Enter the third side of the triangle: "))
if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:
    print("The triangle is valid.")
else:
    print("The triangle is not valid.")


#8.5 Verify Leap Year
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("It's a leap year.")
else:
    print("It's not a leap year.")
