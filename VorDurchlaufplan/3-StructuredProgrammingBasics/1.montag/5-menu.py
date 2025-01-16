# Make a program that asks you for 2 numbers, and lets you perform different
# operations, change the inputs and before exiting shows you
# the activity performed with the program


flag = ""
print("Insert the numbers to operate: ")
a = int(input("a. "))
b = int(input("b. "))
id = 0
operations = []
operations.append([id,a,b,[]])

print("""
    Menu:
        1. Addition
        2. Substraction
        3. Multiplication
        4. Division
        5. Change input
        6. Exit
    """)

while flag != 6:
    flag = int(input("-> "))
    operations[id][3].append(flag)
    if flag == 1:
        c = a + b
        print(a, "+", b, "=", c)
    elif flag == 2:
        c = a - b
        print(a, "-", b, "=", c)
    elif flag == 3:
        c = a * b
        print(a, "x", b, "=", c)
    elif flag == 4:
        c = a / b
        print(a, "/", b, "=", c)
    elif flag == 5:
        print("Insert the numbers to operate: ")
        a = int(input("a. "))
        b = int(input("b. "))
        id += 1
        operations.append([id,a,b,[]])
        print("""
            Menu:
                1. Addition
                2. Substraction
                3. Multiplication
                4. Division
                5. Change input
                6. Exit
            """)

print("Operations done:")
for i in operations: print(i)

print("Exiting...")

