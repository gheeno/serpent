student_score = input("Input a list of student scores ")
student_score_ = list(map(int, filter(None, student_score.split(' '))))
print(student_score_)
height_ = 0

for height in student_score_:
    if height > height_:
        height_ = height

print(f"The highest score in the class is: {height_}")