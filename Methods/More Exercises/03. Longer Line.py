import math


def line(x1, y1, x2, y2):
    x = abs(x1 - x2)
    y = abs(y1 - y2)
    hypotenuse = math.sqrt((x * x) + (y * y))
    return hypotenuse


def closer_line(x, y):
    hypotenuse = math.sqrt((x * x) + (y * y))
    return hypotenuse


one_x_1 = float(input())
one_y_1 = float(input())
one_x_2 = float(input())
one_y_2 = float(input())
two_x_1 = float(input())
two_y_1 = float(input())
two_x_2 = float(input())
two_y_2 = float(input())

if line(one_x_1, one_y_1, one_x_2, one_y_2) >= line(two_x_1, two_y_1, two_x_2, two_y_2):
    if closer_line(one_x_1, one_y_1) < closer_line(one_x_2, one_y_2):
        print(f"({int(one_x_1)}, {int(one_y_1)})({int(one_x_2)}, {int(one_y_2)})")
    else:
        print(f"({int(one_x_2)}, {int(one_y_2)})({int(one_x_1)}, {int(one_y_1)})")
else:
    if closer_line(two_x_1, two_y_1) < closer_line(two_x_2, two_y_2):
        print(f"({int(two_x_1)}, {int(two_y_1)})({int(two_x_2)}, {int(two_y_2)})")
    else:
        print(f"({int(two_x_2)}, {int(two_y_2)})({int(two_x_1)}, {int(two_y_1)})")
