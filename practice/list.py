class CustomList:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return "List is empty"

    def slice(self, start, end):
        return self.items[start:end]

    def is_empty(self):
        return len(self.items) == 0

# Example usage:
my_list = CustomList()
my_list.push(1)
my_list.push(2)
my_list.push(3)

print("Original list:", my_list.items)

popped_item = my_list.pop()
print("Popped item:", popped_item)

print("After popping:", my_list.items)

sliced_items = my_list.slice(0, 2)
print("Sliced items:", sliced_items)

# push = list.append(n)'
# - adds item at the end of the list

# pop = list.pop()
# - removes item at the end of the list.

# slice = list[start:end]
# - retain the start and end index value , delete the rest. 
