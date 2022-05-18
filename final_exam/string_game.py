string = input()
command_args = input().split(" ")

cut_string = ''
is_ended = False
count = -1
cut_count = 0
while command_args[0] != "Done":
    command = command_args[0]
    if command == "Change":
        char = command_args[1]
        replacement = command_args[2]
        for symbol in string:
            if symbol == char:
                string = string.replace(char, replacement)
        print(string)
    elif command == "Includes":
        include_substring = command_args[1]
        if include_substring in string:
            print("True")
        else:
            print("False")
    elif command == "End":
        end_substring = command_args[1]
        print(string.endswith(end_substring))
    elif command == "Uppercase":
        string = string.upper()
        print(string)
    elif command == "FindIndex":
        index_char = command_args[1]
        for symbol in string:
            count += 1
            if symbol == index_char:
                print(count)
                break
    elif command == "Cut":
        start_index = int(command_args[1])
        count = int(command_args[2])
        for i in range(len(string)):
            if cut_count == count:
                print(cut_string)
                break
            if i >= start_index:
                cut_string += string[i]
                cut_count += 1
    command_args = input().split(" ")
