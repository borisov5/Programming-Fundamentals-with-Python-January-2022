number = int(input())
for row in range(number):
    text = input()
    name = ""
    age = ""
    read_name = False
    read_age = False
    for symbol in text:
        if symbol == "@":
            read_name = True
        elif symbol == "|":
            read_name = False
        elif read_name:
            name += symbol
        if symbol == "#":
            read_age = True
        elif symbol == "*":
            read_age = False
        elif read_age:
            age += symbol
    print(f"{name} is {age} years old.")
