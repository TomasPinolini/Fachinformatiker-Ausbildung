import csv

usersfp = r"C:\xampp\Work\3-StructuredProgrammingBasics\3.mittwoch\users_data_cat.csv"
opsfp = r"C:\xampp\Work\3-StructuredProgrammingBasics\3.mittwoch\operations_cat.csv"
logged = False
userid = ""
flag = ""
first = ""
second = ""
operations = []
cate = ""

def login(u, log):
    while not log:
        with open(u, "r") as usersFile:
            usersFile.seek(0)
            username = input("Username: ")
            password = input("Password: ")

            for user in usersFile:
                info = user.split(",")
                if username == info[2] and password == info[3]:
                    log = True
                    uid = info[0]
                    c = info[5]
            
            if not log:
                print("No user with those credentials...", username, password)
    return uid, c

def inputNumbers():
    print("Insert the numbers to operate: ")    
    while True:
        f = input("a. ")
        s = input("b. ")
        try:
            f = int(f)
            s = int(s)
            break
        except ValueError:
            print("Invalid input, insert numbers please!")
    ops = []
    return f, s, ops

def storeInfo(uid, o, a, b, ops):
    with open(o, mode="a", newline='', encoding='utf-8') as operationsFile:
            writer = csv.writer(operationsFile)
            writer.writerow([uid, str(a), str(b), str(ops)])
            # print(f"Rta: {[uid, str(a), str(b), str(ops)]}")
    ops = []
    return ops

def showMenu():
    print("""
        Menu:
            1. Addition
            2. Substraction
            3. Multiplication
            4. Division
            5. Change input
            6. List 
            7. Log out
            8. Close
        """)

def inputMenu():
    while True:
        f = input("-> ")
        try:
            f = int(f)
            if f in range(1,9):
                break
        except ValueError:
            print("Invalid input, insert a number from the menu please!")

    operations.append(f)
    return f

def showOps():
    with open(opsfp, "r") as oF:
        for op in oF:
            print(op)



userid, cate = login(usersfp, logged)
first, second, operations = inputNumbers()
showMenu()


while flag != 8:
    flag = inputMenu()

    if flag == 1:
        c = first + second
        print(first, "+", second, "=", c)
    
    elif flag == 2:
        c = first - second
        print(first, "-", second, "=", c)
    
    elif flag == 3:
        c = first * second
        print(first, "x", second, "=", c)
    
    elif flag == 4:
        if second != 0:
            c = first / second
            print(first, "/", second, "=", c)
        else:
            print("You are trying to divide by 0! Danger!")       
    
    elif flag == 5:
        storeInfo(userid, opsfp, first, second, operations)
        first, second, operations = inputNumbers()
        showMenu()
        
    elif flag == 6:
        if cate == "o":
            showOps()
        else: 
            print("Option only available for owners...")

    elif flag == 7:
        storeInfo(userid, opsfp, first, second, operations)
        print("Logging out...")
        logged = False
        userid, cate = login(usersfp, logged)        
        first, second, operations = inputNumbers()
        showMenu()
  
    else: storeInfo(userid, opsfp, first, second, operations)

