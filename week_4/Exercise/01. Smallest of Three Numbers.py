def smallest_number(a, b, c):
    if a < b and a < c:
        return a
    elif b < a and b < c:
        return b
    else:
        return c

first_num = int(input())
second_num = int(input())
third_num = int(input())
result = smallest_number(first_num, second_num, third_num)
print(result)
