def rage_quit():
    text = input().upper()
    used_unique_symbols = []
    rage_message = ""
    letter = ""
    number = ""
    counter = len(text)
    for symbol in text:
        if symbol.isdigit():
            number += symbol
        else:
            if number != "":
                rage_message += int(number) * letter
                letter = ""
                number = ""
            letter += symbol
            if symbol not in used_unique_symbols:
                used_unique_symbols.append(symbol)
        counter -= 1
        if counter == 0:
            rage_message += letter * int(number)

    print(f"Unique symbols used: {len(used_unique_symbols)}")
    print(rage_message)

rage_quit()