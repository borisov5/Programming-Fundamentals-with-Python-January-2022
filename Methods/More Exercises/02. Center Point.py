import math


def hypotenuse(x, y):
    longest_line = math.sqrt((x * x) + (y * y))
    return longest_line


x_one = float(input())
y_one = float(input())
x_two = float(input())
y_two = float(input())

if hypotenuse(x_one, y_one)) <= hypotenuse(x_two, y_two):
    print(f"({int(x_one)}, {int(y_one)})")
else:
    print(f"({int(x_two)}, {int(y_two)})")
