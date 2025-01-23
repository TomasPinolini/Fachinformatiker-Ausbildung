#8.1 Using break to Exit a Loop.
while True:
    number = int(input("Enter a number (enter 0 to stop): "))
    if number == 0:
        print("Loop stopped.")
        break
    print("You entered:", number)


#8.2 Using continue to Skip an Iteration.
for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i, "is odd")


#8.3 Using pass as a Placeholder.
for i in range(1, 6):
    if i == 3:
        pass  # Placeholder for future code
    print("Processing number:", i)