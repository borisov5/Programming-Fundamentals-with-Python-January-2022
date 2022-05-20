import sys
numbers = input().split(" ")
command = input().split(" ")
max_value = -sys.maxsize
max_index = 0
min_value = sys.maxsize
min_index = 0
first_list = []
last_list = []

while command[0] != "end":

    if command[0] == "exchange":
        index = int(command[1])
        if 0 <= index < len(numbers):
            for i in range(0, index + 1):
                numbers.append(numbers[i])
            for i in range(0, index + 1):
                numbers.remove(numbers[0])
        else:
            print("Invalid index")

    elif command[0] == "max":
        if command[1] == "even":
            for i in range(0, len(numbers)):
                if int(numbers[i]) % 2 == 0 and int(numbers[i]) > max_value:
                    max_value = int(numbers[i])
                    max_index = i
            if max_value == -sys.maxsize:
                print("No matches")
            else:
                print(max_index)

        elif command[1] == "odd":
            for i in range(0, len(numbers)):
                if int(numbers[i]) % 2 == 1 and int(numbers[i]) > max_value:
                    max_value = int(numbers[i])
                    max_index = i
            if max_value == -sys.maxsize:
                print("No matches")
            else:
                print(max_index)

    elif command[0] == "min":
        if command[1] == "even":
            for i in range(0, len(numbers)):
                if int(numbers[i]) % 2 == 0 and int(numbers[i]) < min_value:
                    min_value = int(numbers[i])
                    min_index = i
            if min_value == sys.maxsize:
                print("No matches")
            else:
                print(min_index)
        elif command[1] == "odd":
            for i in range(0, len(numbers)):
                if int(numbers[i]) % 2 == 1 and int(numbers[i]) < min_value:
                    min_value = int(numbers[i])
                    min_index = i
            if min_value == sys.maxsize:
                print("No matches")
            else:
                print(min_index)

    elif command[0] == "first":
        count = int(command[1])
        if count > len(numbers):
            print("Invalid count")
        else:
            if command[2] == "even":
                for i in range(0, len(numbers)):
                    if int(numbers[i]) % 2 == 0:
                        first_list.append(int(numbers[i]))
                        count -= 1
                    if count == 0:
                        break
                print(first_list)
                first_list = []
            elif command[2] == "odd":
                for i in range(0, len(numbers)):
                    if int(numbers[i]) % 2 == 1:
                        first_list.append(int(numbers[i]))
                        count -= 1
                    if count == 0:
                        break
                print(first_list)
                first_list = []

    elif command[0] == "last":
        count = int(command[1])
        if count > len(numbers):
            print("Invalid count")
        else:
            if command[2] == "even":
                for i in range(len(numbers) - 1, -1, -1):
                    if int(numbers[i]) % 2 == 0:
                        last_list.append(int(numbers[i]))
                        count -= 1
                    if count == 0:
                        break
                print(last_list[::-1])
                last_list = []
            elif command[2] == "odd":
                for i in range(len(numbers) - 1, -1, -1):
                    if int(numbers[i]) % 2 == 1:
                        last_list.append(int(numbers[i]))
                        count -= 1
                    if count == 0:
                        break
                print(last_list[::-1])
                last_list = []

    command = input().split(" ")
    max_value = -sys.maxsize
    min_value = sys.maxsize

numbers = [int(number) for number in numbers]
print(numbers)
