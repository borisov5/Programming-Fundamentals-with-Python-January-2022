n = int(input())
#wagons = [0 for x in range(n)]
wagons = [0] * n
comand_input = input()
while comand_input != "End":
    command_args = comand_input.split(" ")
    command = command_args[0]
    first_num = int(command_args[1])
    if command == "add":
        wagons[-1] += first_num
    elif command == "insert":
        second_num = int(command_args[2])
        wagons[first_num] += second_num
    elif command == "leave":
        second_num = int(command_args[2])
        wagons[first_num] -= second_num
    comand_input = input()
print(wagons)
