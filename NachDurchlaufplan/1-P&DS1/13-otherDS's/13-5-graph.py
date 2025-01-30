#1.5.1 Represent and Traverse a Graph Using Adjacency List.
graph = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "D"],
    "D": ["B", "C"]
}

# Traversing and displaying the adjacency list
print("Graph adjacency list:")
for node in graph:
    print(node, "->", graph[node])

    
#1.5.2 Perform BFS Without Functions.
from collections import deque

graph = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "D"],
    "D": ["B", "C"]
}

queue = deque(["A"])
visited = set()

print("BFS Traversal:", end=" ")
while queue:
    node = queue.popleft()
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        queue.extend(graph[node])


#1.5.3 Perform DFS Without Functions
graph = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "D"],
    "D": ["B", "C"]
}

stack = ["A"]
visited = set()

print("DFS Traversal:", end=" ")
while stack:
    node = stack.pop()
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        stack.extend(reversed(graph[node]))


#1.5.4 Find the Degree of a Node in a Graph
node = input("Enter a node to find its degree: ")
if node in graph:
    print(f"Degree of {node}:", len(graph[node]))
else:
    print(f"Node {node} not found in the graph.")
