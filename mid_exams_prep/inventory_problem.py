collected_items = input().split(", ")
command = input().split(" - ")
position = 0
while command[0] != "Craft!":
    if command[0] == "Collect":
        if command[1] not in collected_items:
            collected_items.append(command[1])
    elif command[0] == "Drop":
        if command[1] in collected_items:
            collected_items.remove(command[1])
    elif command[0] == "Combine Items":
        items = command[1]
        list_items = items.split(":")
        if list_items[0] in collected_items:
            for index in range(0, len(collected_items)):
                if collected_items[index] == list_items[0]:
                    position = index + 1
            collected_items.insert(position, list_items[1])
    elif command[0] == "Renew":
        if command[1] in collected_items:
            collected_items.append(command[1])
            collected_items.remove(command[1])
    command = input().split(" - ")

print(", ".join(str(s) for s in collected_items))
