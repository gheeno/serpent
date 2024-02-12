from collections import deque

my_deque = deque([1,2,3,4,5])

my_deque.append(6)
my_deque.appendleft(-1)

print(my_deque)

l = list(my_deque)
print(l)

from collections import deque
q = deque()
q.append('a')
q.append('b')
q.append('c')
print("Initial queue")
print(q)
print("\nElements dequeued from the queue")
print(q.popleft())
print(q)
print(q.popleft())
print(q)
print(q.popleft())
 
print("\nQueue after removing elements")
print(q)