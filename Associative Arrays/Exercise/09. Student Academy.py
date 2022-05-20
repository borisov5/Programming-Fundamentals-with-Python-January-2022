count = int(input())

grades = {}

for _ in range(count):
    name = input()
    grade = float(input())

    if name not in grades:
        grades[name] = []
    grades[name].append(grade)

filtered_grades = {}

for name, grades in grades.items():
    avg_grade = sum(grades) / len(grades)
    if avg_grade >= 4.5:
        filtered_grades[name] = avg_grade

for name, grade in filtered_grades.items():
    print(f"{name} -> {grade:.2f}")
