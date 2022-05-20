numbers = [int(number) for number in input().split()]
command = input().split()
while command[0] != "end":
    action = command[0]
    if action == "swap":
        position_one = int(command[1])
        number_one = numbers[position_one]
        position_two = int(command[2])
        number_two = numbers[position_two]
        numbers[position_one] = number_two
        numbers[position_two] = number_one
    elif action == "multiply":
        numbers[int(command[1])] *= numbers[int(command[2])]
    elif action == "decrease":
        for index in range(0, len(numbers)):
            numbers[index] -= 1
    command = input().split()

print(', '.join(str(number) for number in numbers))
