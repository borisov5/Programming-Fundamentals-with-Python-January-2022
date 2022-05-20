def emoticon_finder():
    text = input()
    emoticons = []
    counter = 0

    for symbol in text:
        counter += 1
        emoticon = ""
        if symbol == ":":
            emoticon += symbol
            emoticon += text[counter]
            emoticons.append(emoticon)

    return emoticons


for emoticon in emoticon_finder():
    print(emoticon)
