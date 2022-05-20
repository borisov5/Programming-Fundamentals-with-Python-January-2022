emplyee_one = int(input())
emplyee_two = int(input())
emplyee_three = int(input())
number_of_students = int(input())
students_per_hour = emplyee_one + emplyee_two + emplyee_three
hours = 0

while number_of_students > 0:
    hours += 1
    if hours % 4 == 0:
        continue
    number_of_students -= students_per_hour

print(f"Time needed: {hours}h.")
