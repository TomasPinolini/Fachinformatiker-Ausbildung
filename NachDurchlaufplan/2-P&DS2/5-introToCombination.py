#5.1 Count Odd and Even Numbers in a Range.
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


#5.2 Find Numbers Divisible by Both 3 and 5.
start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

for num in range(start, end + 1):
    if num % 3 == 0 and num % 5 == 0:
        print(num, "is divisible by both 3 and 5.")


#5.3 Toggle Bits of Numbers in a Range.
start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

for num in range(start, end + 1):
    toggled = ~num
    print("Original:", num, "Toggled:", toggled)


