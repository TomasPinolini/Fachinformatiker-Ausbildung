#7.1 For Loops Introduction.
for i in range(1, 11):
    print(i)


#7.2 Sum of First N Numbers.
n = int(input("Enter a number: "))
total = 0
for i in range(1, n + 1):
    total += i

print("The sum of numbers from 1 to", n, "is:", total)



#7.3 While Loops.
limit = int(input("Enter a number: "))

# Print numbers starting from 1 until the limit.
i = 1
while i <= limit:
    print(i)
    i += 1


#7.4 Keep Asking Until a Condition is Met.
num = int(input("Enter a number (enter 0 to stop): "))

while num != 0:
    print("You entered:", num)
    num = int(input("Enter another number (enter 0 to stop): "))

print("Goodbye!")
