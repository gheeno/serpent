class ListSorter:
    def __init__(self, list):
        self.list = list

    def print_list(self):
        return self.list
    
    def get_list(self, index):
        return self.list[index]
    
    def get_highest(self):
        e = 0
        for i, v in enumerate(self.list):
            if v > e:
                e = v
        return f"value : {e} index : {i}"
    
    def get_number_of_items_in_list(self):
        return len(self.list)
    
    def print_for_loop(self):
        for i in range(1,10): #prints 1 to 9
            print(i)

    
l = [1,11,13,23,14,25]

ls = ListSorter(l)
print(ls.print_list())
index = 0
print(f"List value of {ls.get_list(index)} at index {index}")
print(ls.get_highest())
print("Number of items in list : ", ls.get_number_of_items_in_list())
ls.print_for_loop()