## Check if in a list all elements are positive, introducing flagging
l = [1,2,-3,4,5]
flag = True
# for i in l:
#     if i < 0:
#         flag = False
#     elif i == 0:
#         flag = False

# if flag: print(":)")
# else: print(":(")

## Ask for input until a '.' is entered, insert the letters into an array
while flag:
    flag = input("-> ")
    if flag == ".":
        flag = False