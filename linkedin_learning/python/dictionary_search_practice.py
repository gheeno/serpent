class DictionaryUtility():
    def __init__(self, dictionary):
        self.dictionary = dictionary

    def get_value(self, language):
        return self.dictionary[language]
    
    def get_key(self, points):
        return list(self.dictionary.keys())[list(self.dictionary.values()).index(points)]

    def level_of_confidence(self):
        return sorted(self.dictionary.items())
    
    def key_list(self):
        return list(self.dictionary.keys())
    
    def value_list(self):
        return list(self.dictionary.values())
    
    def value_index(self, points): #get the index of the points.
        return self.value_list().index(points)
    
    def key_index(self, value): #use the index to get the key.
        return self.key_list()[value]
    
    def most_points(self):
        c = 0
        for i in self.dictionary.values():
            if i > c :
                c = i
        index = list(self.dictionary.values()).index(c)
        lang = list(self.dictionary.keys())[index]
        return lang
            
# Example dictionary : 
dict = {
    "Java" : 50,
    "C++" : 10, 
    "C#" : 10,
    "Python" : 80
}

du = DictionaryUtility(dict)
# print("Sorted : ",du.level_of_confidence())
# print("Get Key : ", du.get_key(80))
# print("Get Value : ", du.get_value("Python"))
# print("Key List", du.key_list())
# print("Value List", du.value_list())
# vindex = du.value_index(80)
# print("Value index : ", vindex)
# print("Key index : ", du.key_index(vindex))
print("Highest points : ", du.most_points())

