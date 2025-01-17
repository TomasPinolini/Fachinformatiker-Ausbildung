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
