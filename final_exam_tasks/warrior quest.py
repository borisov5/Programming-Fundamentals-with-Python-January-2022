text = input()
command = input().split(" ")

while True:
    if command[0] == "For" and command[1] == "Azeroth":
        break

    if command[0] == "GladiatorStance":
        text = text.upper()
        print(text)
    elif command[0] == "DefensiveStance":
        text = text.lower()
        print(text)
    elif command[0] == "Dispel":
        index = int(command[1])
        letter = command[2]
        if 0 <= index < len(text):
            text = text.replace(text[index], letter, 1)
            print("Success!")
        else:
            print("Dispel too weak.")
    elif command[0] == "Target":
        if command[1] == "Change":
            first_substring = command[2]
            second_substring = command[3]
            if first_substring in text:
                text = text.replace(first_substring, second_substring)
                print(text)
        elif command[1] == "Remove":
            substring = command[2]
            if substring in text:
                text = text.replace(substring, "")
                print(text)
        else:
            print("Command doesn't exist!")
    else:
        print("Command doesn't exist!")
    command = input().split(" ")
