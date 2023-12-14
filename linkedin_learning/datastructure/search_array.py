list = [1, 2, 1, 4, 5, 6, 7]
ITEM = 1

# linear - sequential search.
# O(n)

def search(item, _list):
    for i in _list:
        print(i)
        if i == item:
            return True
        
print(search(ITEM, list))