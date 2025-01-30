#1.1.1 Implement a Simple Queue.
from collections import deque

queue = deque()

# Enqueue
queue.append("A")
queue.append("B")
queue.append("C")
print("Queue after enqueue:", list(queue))

# Dequeue
queue.popleft()
print("Queue after dequeue:", list(queue))


#1.1.2 Implement a Queue with a Limit.
from collections import deque

queue = deque()
max_size = 3

queue.append("A")
queue.append("B")
queue.append("C")
print("Queue:", list(queue))

if len(queue) == max_size:
    print("Queue is full. Removing oldest element.")
    queue.popleft()

queue.append("D")
print("Queue after adding a new element:", list(queue))


#1.1.3 Peek the Front of the Queue
queue = deque(["X", "Y", "Z"])
print("Front element of the queue:", queue[0])


#1.1.4 Reverse a Queue
queue = deque(["A", "B", "C"])
queue.reverse()
print("Reversed queue:", list(queue))
