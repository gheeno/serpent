my_list = [1, 7, 3]
print(sorted(my_list, reverse=True))

student_grades = [('Sarah', 90), ('Rebecca', 82), ('Matt', 91)]
print(sorted(student_grades))
# lamda tells the sorted function to look at the 
# "grades, index 1 ( remember index starts at 0 ) , and then thats the key. "
# the "key" is then sorted.
print(sorted(student_grades, key=lambda x:x[1], reverse=True ))

# Time Complexity : O(n)