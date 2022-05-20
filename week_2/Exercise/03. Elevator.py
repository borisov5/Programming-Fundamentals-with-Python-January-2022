import math
number_of_people = int(input())
capacity = int(input())

number_of_courses = math.ceil(number_of_people / capacity)

print(number_of_courses)
