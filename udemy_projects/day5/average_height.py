student_heights = input("Input a list of student heights ")
student_heights_ = list(map(int, filter(None, student_heights.split(' '))))
total_height = 0

for height in student_heights_:
    total_height += height

average_height = total_height / len(student_heights_)
print(round(average_height))