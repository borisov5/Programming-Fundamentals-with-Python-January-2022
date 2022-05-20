chat = []
command = input().split(" ")
while True:
    if command[0] == "end":
        break
    elif command[0] == "Chat":
        message = command[1]
        chat.append(message)
    elif command[0] == "Delete":
        message = command[1]
        if message in chat:
            chat.remove(message)
    elif command[0] == "Edit":
        message = command[1]
        edited_version = command[2]
        if message in chat:
            for i in range(len(chat)):
                if message == chat[i]:
                    chat.remove(message)
                    chat.insert(i, edited_version)
    elif command[0] == "Pin":
        message = command[1]
        if message in chat:
            chat.remove(message)
            chat.append(message)
    elif command[0] == "Spam":
        for index in range(1, len(command)):
            chat.append(command[index])
    command = input().split(" ")

for string in chat:
    print(string)