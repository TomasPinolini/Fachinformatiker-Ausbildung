#1.4.1 Manually Create a Binary Tree.
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Creating nodes
root = Node(10)
root.left = Node(5)
root.right = Node(15)

# Displaying tree structure
print("Root:", root.value)
print("Left child of root:", root.left.value)
print("Right child of root:", root.right.value)


#1.4.2 Manually Traverse a Tree Inorder.
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Creating nodes
root = Node(10)
root.left = Node(5)
root.right = Node(15)
root.left.left = Node(2)
root.left.right = Node(7)

# Inorder traversal without recursion
stack = []
current = root
print("Inorder Traversal:", end=" ")

while stack or current is not None:
    if current is not None:
        stack.append(current)
        current = current.left
    else:
        current = stack.pop()
        print(current.value, end=" ")
        current = current.right