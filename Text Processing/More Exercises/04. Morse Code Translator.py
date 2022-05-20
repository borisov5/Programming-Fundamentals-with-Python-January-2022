text = input().split("|")
translated_text = ""
string_english = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
                  "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
string_morse = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..",
                ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.",
                "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--..", ".----",
                "..---", "...--", "....-", ".....", "-....", "--...", "---..", "----.",
                "-----", "--..--", ".-.-.-", "..--.."]
for word in text:
    letters = word.split(" ")
    for letter in letters:
        counter = 0
        for symbol in string_morse:
            if letter == symbol:
                translated_text += string_english[counter]
            counter += 1
    translated_text += " "
print(translated_text)