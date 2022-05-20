first_line = input().split(" | ")
second_line = input().split(" | ")
command = input()

first_library = []
second_library = []
library = {}
is_printed = False
for symbol in first_line:
    symbol = symbol.split(": ")
    first_library.append(symbol[0])
    second_library.append(symbol[1])

if command == "Hand Over":
    print(" ".join(first_library))


elif command == "Test":
    for word_args in first_line:
        word_args = word_args.split(": ")
        key = word_args[0]
        value = word_args[1]
        if key in second_line:
            if is_printed == False:
                print(f"{key}")
                print(f" -{value}")
                is_printed = True
            else:
                print(f" -{value}")
