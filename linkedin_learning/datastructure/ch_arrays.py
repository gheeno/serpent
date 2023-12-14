# create a function that finds the second smallest item.
# input [9,3,10,2,6]
# ouput 3
# list can be empty
# if list = output none.


# def find_second_smallest(my_list):
#     lindex = my_list[0]
#     nindex = []

#     if my_list == None:
#         return None
    
#     if len(my_list) == 1:
#         return "Only 1 value on list."

#     for i in my_list:
#         if lindex > i:
#             nindex.append(i)
    
#     cindex = nindex[0]
#     for i in nindex:
#         if cindex > i:
#             return cindex

#Chat GPT
def find_second_smallest(my_list):
    if my_list is None or len(my_list) == 0:
        return None
    
    if len(my_list) == 1:
        return "Only 1 value in the list."

    smallest = float('inf')
    second_smallest = float('inf')

    for num in my_list:
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif num < second_smallest and num != smallest:
            second_smallest = num

    if second_smallest == float('inf'):
        return "No distinct second smallest element found."
    
    return second_smallest


print(find_second_smallest([5, 8, 3, 2, 6, 4, 7]))