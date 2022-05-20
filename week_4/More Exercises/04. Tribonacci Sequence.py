def tribonacci(num):
    list = []
    current_number = 1
    previous_one = 0
    previous_two = 0
    previous_three = 0
    for number in range(num):
        list.append(str(current_number))
        previous_one = previous_two
        previous_two = previous_three
        previous_three = current_number
        current_number = (previous_one + previous_two + previous_three)
    return list

number = int(input())
print(" ".join(tribonacci(number)))