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