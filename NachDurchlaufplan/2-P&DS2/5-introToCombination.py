<<<<<<< HEAD
#10.1 Count Odd and Even Numbers in a Range.
=======
#5.1 Count Odd and Even Numbers in a Range.
>>>>>>> 24e39dae881d2a8ddfea838b6b80ca5293a3a5e4
start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

odd_count = 0
even_count = 0

for num in range(start, end + 1):
    if num & 1 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Total even numbers:", even_count)
print("Total odd numbers:", odd_count)


<<<<<<< HEAD
#10.2 Find Numbers Divisible by Both 3 and 5.
=======
#5.2 Find Numbers Divisible by Both 3 and 5.
>>>>>>> 24e39dae881d2a8ddfea838b6b80ca5293a3a5e4
start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

for num in range(start, end + 1):
    if num % 3 == 0 and num % 5 == 0:
        print(num, "is divisible by both 3 and 5.")


<<<<<<< HEAD
#10.3 Toggle Bits of Numbers in a Range.
=======
#5.3 Toggle Bits of Numbers in a Range.
>>>>>>> 24e39dae881d2a8ddfea838b6b80ca5293a3a5e4
start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

for num in range(start, end + 1):
    toggled = ~num
    print("Original:", num, "Toggled:", toggled)


<<<<<<< HEAD
=======
#5.4 Find the LCM of Two Numbers.
def lcm(a, b):
    from math import gcd
    return abs(a * b) // gcd(a, b)

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
print("The LCM of", num1, "and", num2, "is:", lcm(num1, num2))


#5.5 Find All Prime Numbers in a Range.
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))
primes = [num for num in range(start, end + 1) if is_prime(num)]
print("Prime numbers in the range:", primes)
>>>>>>> 24e39dae881d2a8ddfea838b6b80ca5293a3a5e4
