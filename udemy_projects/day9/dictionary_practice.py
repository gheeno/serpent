student_scores = {
    "Harry": 81,
    "Barry": 90,
    "Brian": 40,
    "Mark": 1,
    "Ace": 2,
}

#TODO : 
# 1. Create an empty dictionary called student_grades
student_grades = {}

# 2. write your code  below to add the grades of the student.
# spec : 
# 1. Scores 91, 100 : Outstanding
# 2. Scores 81, 90 : "Exceed Expectations"
# 3. Scores 71, 80 : "Acceptable"
# 4. Scores below 70 : "Failed"

#Expected Output:
# { "Harry" : "Exceeds expectation", "Barry" : "Outstanding"}

for key in student_scores:
    if student_scores[key] >= 91 or student_scores[key] == 100:
        student_grades[key] = "Outstanding"
    elif student_scores[key] >= 81 or student_scores[key] == 90:
        student_grades[key] = "Exceed Expectations"
    elif student_scores[key] >= 71 or student_scores[key] ==80:
        student_grades[key] = "Acceptable"
    else:
        student_grades[key] = "Failed"

print(student_grades)