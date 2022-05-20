def print_round_value_of_numbers():
    args = input().split(" ")
    numbers = []

    for arg in args:
        num = float(arg)
        abs_num = round(num)
        numbers.append(abs_num)

    print(numbers)

print_round_value_of_numbers()