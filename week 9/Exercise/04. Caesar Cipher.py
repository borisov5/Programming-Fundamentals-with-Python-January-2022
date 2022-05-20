def encryption():
    text = input()
    encrypted_text = ""
    for symbol in text:
        encrypted_text += chr(ord(symbol) + 3)

    return encrypted_text


print(encryption())
