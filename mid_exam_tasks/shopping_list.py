groceries = input().split("!")
command = input().split(" ")
position = 0
while command[0] != "Go" and command[1] != "Shopping!":
    if command[0] == "Urgent":
        if command[1] not in groceries:
            groceries.insert(0, command[1])
    elif command[0] == "Unnecessary":
        if command[1] in groceries:
            groceries.remove(command[1])
    elif command[0] == "Correct":
        if command[1] in groceries:
            for index in range(0, len(groceries)):
                if groceries[index] == command[1]:
                    position = index
                    groceries.insert(position, command[2])
                    groceries.remove(command[1])
    elif command[0] == "Rearrange":
        if command[1] in groceries:
            groceries.append(command[1])
            groceries.remove(command[1])
    command = input().split(" ")

print(", ".join(str(s) for s in groceries))
