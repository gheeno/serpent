class TupleUtility:
    def __init__(self, tup):
        self.tuple = tup

    # def get_highest_number(self):
    #     return max(self.tuple)

    # def get_lowest_number(self):
    #     return min(self.tuple)

    def get_highest_number(self):
        max = 0 
        for v in self.tuple:
            if v > max:
                max = v
        return max
    
    def get_lowest_number(self):
        min = self.tuple[0]
        for v in self.tuple:
            if v < min: 
                min = v
        return min

t = (1,2,3,4,5,6,7,8,9,10)

tup1 = TupleUtility(t)
print(tup1.get_highest_number())
print(tup1.get_lowest_number())