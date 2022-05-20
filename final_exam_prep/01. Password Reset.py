def take(text):
    new_text = ""
    for index in range(1, len(text), 2):
        new_text += text[index]
    return new_text


def cut(text, i, taken_length):
    text = list(text)
    for _ in range(taken_length):
        removed_symbol = text.pop(i)
    return "".join(text)


def substitute(text, string_one, string_two):
    replaced_text = text.replace(string_one, string_two)
    return replaced_text


password = input()
command = input().split(" ")
while command[0] != "Done":
    if command[0] == "TakeOdd":
        password = take(password)
        print(password)
    elif command[0] == "Cut":
        index = int(command[1])
        length = int(command[2])
        password = cut(password, index, length)
        print(password)
    elif command[0] == "Substitute":
        containing_string = command[1]
        string_for_replace = command[2]
        if containing_string in password:
            password = substitute(password, containing_string, string_for_replace)
            print(password)
        else:
            print("Nothing to replace!")
    command = input().split(" ")

print(f"Your password is: {password}")
