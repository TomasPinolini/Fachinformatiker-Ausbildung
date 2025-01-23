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


#1.4.2 Manually Traverse a Tree In order.
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

# In order traversal without recursion
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


#1.4.3 Calculate the Height of a Binary Tree
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def height(node):
    if node is None:
        return 0
    left_height = height(node.left)
    right_height = height(node.right)
    return max(left_height, right_height) + 1

# Create binary tree
root = Node(10)
root.left = Node(5)
root.right = Node(15)
root.left.left = Node(2)
root.left.right = Node(7)

print("Height of the binary tree:", height(root))


#1.4.4 Count the Nodes in a Binary Tree
def count_nodes(node):
    if node is None:
        return 0
    return 1 + count_nodes(node.left) + count_nodes(node.right)

print("Total number of nodes in the tree:", count_nodes(root))
