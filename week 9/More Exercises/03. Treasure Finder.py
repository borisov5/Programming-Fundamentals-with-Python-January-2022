keys = input().split(" ")

while True:
    text = input()
    if text == "find":
        break
    hidden_message = ""
    key_index = 0
    for index in range(len(text)):
        if key_index == len(keys):
            key_index = 0
        symbol = chr(ord(text[index]) - int(keys[key_index]))
        hidden_message += symbol
        key_index += 1

    read_counter = 0
    type = ""
    coordinates = ""
    read_type = False
    read_coordinates = False
    for symbol in hidden_message:
        if symbol == "&":
            read_type = True
            read_counter += 1
        elif read_counter == 2:
            read_name = False
        elif read_type:
            type += symbol
        if symbol == "<":
            read_coordinates = True
        elif symbol == ">":
            read_coordinates = False
        elif read_coordinates:
            coordinates += symbol
    print(f"Found {type} at {coordinates}")
