class LinkedListNode():
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

class LinkedList():
    def __init__(self, head=None):
        self.head = head

    def insert(self, value):
        node = LinkedListNode(value)
        if self.head is None:
            self.head = node
        current_node = self.head
        while True:
            if current_node.next_node is None:
                current_node.next_node = node
                break
            current_node = current_node.next_node

    def print_linked_list(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.value, "->", end='')
            current_node = current_node.next_node
        print("None")

list = LinkedList()
list.insert('1')
list.print_linked_list()
