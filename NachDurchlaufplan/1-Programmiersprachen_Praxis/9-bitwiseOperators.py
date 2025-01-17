#9.1 Check if a Number is Even or Odd Using Bitwise AND.
num = int(input("Enter a number: "))
if num & 1 == 0:
    print("The number is even.")
else:
    print("The number is odd.")


#9.2 Find the Result of Bitwise OR.
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
result = num1 | num2
print("The result of bitwise OR is:", result)


#9.3 Swap Two Numbers Using Bitwise XOR.
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

a = a ^ b
b = a ^ b
a = a ^ b

print("After swapping, a =", a, "and b =", b)


#9.4 Check if a Bit is Set at a Specific Position.
num = int(input("Enter a number: "))
position = int(input("Enter the bit position to check (0-based): "))

if num & (1 << position):
    print("The bit at position", position, "is set (1).")
else:
    print("The bit at position", position, "is not set (0).")


#9.5 Set a Specific Bit in a Number.
num = int(input("Enter a number: "))
position = int(input("Enter the bit position to set (0-based): "))

num = num | (1 << position)
print("The new number after setting the bit is:", num)


#9.6 Clear a Specific Bit in a Number.
num = int(input("Enter a number: "))
position = int(input("Enter the bit position to clear (0-based): "))

num = num & ~(1 << position)
print("The new number after clearing the bit is:", num)