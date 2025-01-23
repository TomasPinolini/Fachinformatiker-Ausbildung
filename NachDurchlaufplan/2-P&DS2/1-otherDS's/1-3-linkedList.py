#1.3.1 Manually Create and Traverse a Linked List.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Creating nodes
head = Node(10)
second = Node(20)
third = Node(30)

# Linking nodes
head.next = second
second.next = third

# Traversing the linked list
current = head
while current is not None:
    print(current.data)
    current = current.next


#1.3.2 Add a Node at the End.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Creating nodes
head = Node(10)
second = Node(20)

# Linking nodes
head.next = second

# Adding a new node at the end
new_node = Node(30)
second.next = new_node

# Traversing the linked list
current = head
while current is not None:
    print(current.data)
    current = current.next


#1.3.3 Delete a Node from the Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Create linked list
head = Node(10)
second = Node(20)
third = Node(30)
head.next = second
second.next = third

# Delete the second node
head.next = head.next.next

# Traverse the list
current = head
while current:
    print(current.data)
    current = current.next


#1.3.4 Search for a Value in the Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Create linked list
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)

# Search for a value
search_value = int(input("Enter a value to search for: "))
current = head
found = False
while current:
    if current.data == search_value:
        found = True
        break
    current = current.next

if found:
    print(f"Value {search_value} found in the list.")
else:
    print(f"Value {search_value} not found in the list.")
