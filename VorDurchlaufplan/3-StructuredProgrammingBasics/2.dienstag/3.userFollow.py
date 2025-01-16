# Add a login so only authorized users get access.
# Let them change users throught the session.
# Before shutting the programm, show them a list of sessions with all the information gatherable.


userInfo = [[0, "tomas", "12345"],[1, "michael", "12345"]]
logged = False

while not logged:
    username = input("Username: ")
    password = input("Password: ")
    infoEntered = [username, password]

    for user in userInfo:
        if infoEntered == [user[1], user[2]]:
            logged = True
            userid = user[0]
    
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
operations.append([id,userid,a,b,[]])
print("""
    Menu:
        1. Addition
        2. Substraction
        3. Multiplication
        4. Division
        5. Change input
        6. Log out
        7. Close
    """)

while flag != 7:
    while True:
        flag = input("-> ")
        try:
            flag = int(flag)
            if flag in range(1,8):
                break
        except ValueError:
            print("Invalid input, insert a number from the menu please!")
    
    if flag in range(1,5): operations[id][4].append(flag)

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
        operations.append([id, userid,a,b,[]])
        print("""
            Menu:
                1. Addition
                2. Substraction
                3. Multiplication
                4. Division
                5. Change input
                6. Log Out
                7. Exit
            """)
    elif flag == 6:
        print("Logging out...")
        logged = False
        while not logged:
            username = input("Username: ")
            password = input("Password: ")
            infoEntered = [username, password]

            for user in userInfo:
                if infoEntered == [user[1], user[2]]:
                    logged = True
                    userid = user[0]
            
            if not logged:
                print("No user with those credentials...")
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
        operations.append([id,userid,a,b,[]])
        print("""
            Menu:
                1. Addition
                2. Substraction
                3. Multiplication
                4. Division
                5. Change input
                6. Log out
                7. Close
            """)


print("Operations done:")
for i in operations: print(i)