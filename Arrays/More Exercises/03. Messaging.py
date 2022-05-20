numbers = input().split(" ")
text = list(input())
char = 0
for i in range(0, len(numbers)):
    index = numbers[i]
    for num in range(len(index)):
        char += int(index[num])
    if char > len(text):
        char %= len(text)
    symbol = text[char]
    print(symbol, end = "")
    text.remove(symbol)
    char = 0