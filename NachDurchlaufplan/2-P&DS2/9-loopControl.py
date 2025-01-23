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


#8.4 Nested Loops with Break
for i in range(1, 4):
    for j in range(1, 4):
        if i * j == 4:
            print(f"Breaking at i={i}, j={j}")
            break
    else:
        continue
    break


#8.5 While Loop with Else
num = 5
while num > 0:
    print("Countdown:", num)
    num -= 1
else:
    print("Liftoff!")
