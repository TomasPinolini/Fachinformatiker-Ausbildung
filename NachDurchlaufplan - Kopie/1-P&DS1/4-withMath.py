#4.1 Simple sum.
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
sum_result = num1 + num2
print("The sum is:", sum_result)


#4.2 Rectangle's width and height.
width = float(input("Enter the width of the rectangle: "))
height = float(input("Enter the height of the rectangle: "))
area = width * height
perimeter = 2 * (width + height)
print("Area:", area)
print("Perimeter:", perimeter)


#4.3 Average of three numbers.
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

average = (num1 + num2 + num3) / 3
print("The average of", num1, ",", num2, "and", num3, "is:", average)


#4.4 Total amount and the percentage.
total = float(input("Enter the total amount: "))
percentage = float(input("Enter the percentage to calculate: "))
result = (total * percentage) / 100
print(percentage, "% of", total, "is:", result)


#4.5 Convert minutes to seconds
minutes = float(input("Enter the time in minutes: "))
seconds = minutes * 60
print(minutes, "minutes is equal to", seconds, "seconds.")


#4.6 Calculate the Volume of a Cylinder
radius = float(input("Enter the radius of the cylinder: "))
height = float(input("Enter the height of the cylinder: "))
volume = 3.14159 * radius**2 * height
print("The volume of the cylinder is:", volume)


#4.7 Find the Hypotenuse of a Right Triangle
a = float(input("Enter the length of the first side: "))
b = float(input("Enter the length of the second side: "))
hypotenuse = (a**2 + b**2)**0.5
print("The hypotenuse of the triangle is:", hypotenuse)
