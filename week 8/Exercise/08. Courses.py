data = input()

courses = {}

while not data == "end":
    course_name, student_name = data.split(" : ")

    if course_name not in courses:
        courses[course_name] = []
    courses[course_name].append(student_name)

    data = input()

for course_name, students in courses.items():
    print(f"{course_name}: {len(students)}")
    for name in students:
        print(f"-- {name}")
