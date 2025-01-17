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