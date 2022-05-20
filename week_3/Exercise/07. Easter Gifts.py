gift_list = input().split()
command = input()
last_list = ""

while command != "No Money":
    command_list = command.split()
    command = command_list[0]
    gift = command_list[1]
    if len(command_list) == 3:
        position = int(command_list[2])

    if command == "OutOfStock":
        for index in range(len(gift_list)):
            if gift_list[index] == gift:
                gift_list[index] = None
    elif command == "Required":
        if 0 <= position < len(gift_list):
            gift_list[position] = gift
    elif command == "JustInCase":
        gift_list[len(gift_list) - 1] = gift
    command = input()

for gift in gift_list:
    if gift != None:
        print(gift, end = " ")
