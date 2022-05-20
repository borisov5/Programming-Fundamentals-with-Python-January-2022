import sys
max_number = -sys.maxsize
number_of_students = int(input())
number_of_lectures = int(input())
additional_bonus = int(input())
max_bonus = 0
student_attendences = 0
for i in range(number_of_students):
    current_attendance = int(input())
    current_bonus = current_attendance / number_of_lectures * (5 + additional_bonus)
    if current_bonus > max_number:
        max_number = current_bonus
        student_attendences = current_attendance
        max_bonus = current_bonus

print(f"Max Bonus: {round(max_bonus)}.")
print(f"The student has attended {student_attendences} lectures.")
