import csv
import os

usersfp = r"C:\xampp\Work\3-StructuredProgrammingBasics\2.dienstag\users_data.csv"
opsfp = r"C:\xampp\Work\3-StructuredProgrammingBasics\2.dienstag\operations.csv"
logged = False
userid = ""
flag = ""

#LogIn
while not logged:
    with open(usersfp, "r") as usersFile:
        usersFile.seek(0)
        username = input("Username: ")
        password = input("Password: ")

        for user in usersFile:
            info = user.split(",")
            if username == info[2] and password == info[3]:
                logged = True
                userid = info[0]
                operations = []
        
        if not logged:
            print("No user with those credentials...", username, password)

print("Insert the numbers to operate: ")

#inputNumbers    
while True:
    a = input("a. ")
    b = input("b. ")
    try:
        a = int(a)
        b = int(b)
        break
    except ValueError:
        print("Invalid input, insert numbers please!")

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

    operations.append(flag)

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
    #inputNumbers    
    elif flag == 5:
        with open(opsfp, mode="a", newline='', encoding='utf-8') as operationsFile:
            writer = csv.writer(operationsFile)
            writer.writerow([userid, str(a), str(b), str(operations)])
            print(f"Rta: {[userid, str(a), str(b), str(operations)]}")

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
        operations = []
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
        with open(opsfp, mode="a", newline='', encoding='utf-8') as operationsFile:
            writer = csv.writer(operationsFile)
            writer.writerow([userid, str(a), str(b), str(operations)])
            print(f"Rta: {[userid, str(a), str(b), str(operations)]}")
        operations = []
        print("Logging out...")
        logged = False
        
        #LogIn
        with open(usersfp, "r") as usersFile:
            while not logged:
                usersFile.seek(0)
                username = input("Username: ")
                password = input("Password: ")

                for user in usersFile:
                    info = user.split(",")
                    if username == info[2] and password == info[3]:
                        logged = True
                        userid = info[0]
                        operations = []
                
                if not logged:
                    print("No user with those credentials...")

        #inputNumbers    
        while True:
            a = input("a. ")
            b = input("b. ")
            try:
                a = int(a)
                b = int(b)
                break
            except ValueError:
                print("Invalid input, insert numbers please!")
            
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
    
    else: 
        with open(opsfp, mode="a", newline='', encoding='utf-8') as operationsFile:
            writer = csv.writer(operationsFile)
            writer.writerow([userid, str(a), str(b), str(operations)])
            print(f"Rta: {[userid, str(a), str(b), str(operations)]}")


with open(opsfp, "r") as operationsFile:
    print("Operations registered:")
    for i in operationsFile: print(i)

