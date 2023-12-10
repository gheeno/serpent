class DictionaryUtility: 
    def __init__(self, dct):
        self.dct = dct
        
    def get_lowest_val(self):
        val_list = list(self.dct.values())
        key_list = list(self.dct.keys())

        min_value = val_list[0]
        min_index = 0
        for i, v in enumerate(val_list):
            if v <= min_value:
                min_value = v
                min_index = i
            min_key = key_list[min_index]
        return min_value, min_key

dict = {
    "D" : 100,
    "A" : 10,
    "B" : 15,
    "C" : 90
}

d = DictionaryUtility(dict)
print(d.get_lowest_val())
