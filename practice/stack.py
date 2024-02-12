class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            print("Stack is empty")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            print("Stack is empty")

    def size(self):
        return len(self.items)


# Example usage:
stack = Stack()
print("Is the stack empty?", stack.is_empty())  # Output: True

stack.push(1)
stack.push(2)
stack.push(3)

print("Peek:", stack.peek())  # Output: 3
print("Size:", stack.size())  # Output: 3

print("Pop:", stack.pop())    # Output: 3
print("Pop:", stack.pop())    # Output: 2
print("Pop:", stack.pop())    # Output: 1
print("Pop:", stack.pop())    # Output: Stack is empty

print("Is the stack empty?", stack.is_empty())  # Output: True
