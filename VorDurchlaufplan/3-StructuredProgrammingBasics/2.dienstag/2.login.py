# Add a login so only authorized users get access.

userInfo = [["tomas", "12345"],["michael", "12345"]]
logged = False

while not logged:
    username = input("Username: ")
    password = input("Password: ")
    infoEntered = [username, password]

    for user in userInfo:
        if infoEntered == user:
            logged = True
    
    if not logged:
        print("No user with those credentials...")

flag = ""
print("Insert the numbers to operate: ")
while True:
    a = input("a. ")
    b = input("b. ")
    try:
        a = int(a)
        b = int(b)
        break
    except ValueError:
        print("Invalid input, insert numbers please!")
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
    while True:
        flag = input("-> ")
        try:
            flag = int(flag)
            if flag in range(1,7):
                break
        except ValueError:
            print("Invalid input, insert a number from the menu please!")
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
        if b != 0:
            c = a / b
            print(a, "/", b, "=", c)
        else:
            print("You are trying to divide by 0! Danger!")
    elif flag == 5:
        print("Insert the numbers to operate: ")
        while True:
            a = input("a. ")
            b = input("b. ")
            try:
                a = int(a)
                b = int(b)
                break
            except ValueError:
                print("Invalid input, insert numbers please!")

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