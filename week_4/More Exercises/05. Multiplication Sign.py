def multiplication(one, two, three):
    if one == 0 or two == 0 or three == 0:
        return "zero"
    elif one > 0 and two > 0 and three > 0:
        return "positive"
    elif one < 0 and two < 0 and three > 0:
        return "positive"
    elif one < 0 and two > 0 and three < 0:
        return "positive"
    elif one > 0 and two < 0 and three < 0:
        return "positive"
    else:
        return "negative"

first_num = int(input())
second_num = int(input())
third_num = int(input())
print(multiplication(first_num, second_num, third_num))
