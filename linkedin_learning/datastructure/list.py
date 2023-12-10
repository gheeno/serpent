### LIST
# get the average

student_pet_count_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0, 0, 0]
NUM_OF_STUDENTS = len(student_pet_count_list)
print(NUM_OF_STUDENTS)

#mutate the list 
# replacae index 2 with new pet 5
student_pet_count_list[2] = 5
# student index 2 adds another +1 pet
student_pet_count_list[2] = student_pet_count_list[2] + 1
# new student joined with 1 pet. 
student_pet_count_list[-1] = 1
student_pet_count_list.append(5)
print(student_pet_count_list)

# average = sum / number of items.
total = 0
for v in student_pet_count_list:
    total += v

print(f"Average {total/NUM_OF_STUDENTS:.2f}%")