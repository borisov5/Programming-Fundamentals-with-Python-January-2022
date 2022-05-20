messages = input().split(" ")
decipher = []

for index in range(len(messages)):
    number = ""
    word = ""
    for symbol in messages[index]:
        if symbol.isdigit():
            number += symbol
        else:
            word += symbol
    number = chr(int(number))
    if len(word) > 1:
        word = word[len(word)-1] + word[1:-1] + word[0]
    message = number + word
    decipher.append(message)

print(" ".join(str(s) for s in decipher))
