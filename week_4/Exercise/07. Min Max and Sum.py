def min_number(min_num):
    for num in range(len(min_num)):
        min_num[num] = int(min_num[num])
    result = min(min_num)
    return f"The minimum number is {result}"

def max_number(max_num):
    for num in range(len(max_num)):
        max_num[num] = int(max_num[num])
    result = max(max_num)
    return f"The maximum number is {result}"

def sum_numbers(sum):
    result = 0
    for num in range(len(sum)):
        result += int(sum[num])
    return f"The sum number is: {result}"

numbers = input().split(" ")
print(min_number(numbers))
print(max_number(numbers))
print(sum_numbers(numbers))
