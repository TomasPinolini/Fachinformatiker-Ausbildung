#1.2.1 Push and Pop Operations.
stack = []

# Push elements
stack.append("X")
stack.append("Y")
stack.append("Z")
print("Stack after push:", stack)

# Pop elements
stack.pop()
print("Stack after one pop:", stack)
stack.pop()
print("Stack after another pop:", stack)


#1.2.2 Check if the Stack is Empty.
stack = []

if len(stack) == 0:
    print("The stack is empty.")
else:
    print("The stack is not empty.")

# Push an element
stack.append("A")
print("After pushing an element:", stack)

# Check again
if len(stack) == 0:
    print("The stack is empty.")
else:
    print("The stack is not empty.")