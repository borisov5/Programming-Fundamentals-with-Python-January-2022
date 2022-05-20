first_string = ord(input()) + 1
second_string = ord(input())
text = input()
sum = 0
for symbol in text:
    if ord(symbol) in range(first_string, second_string):
        sum += ord(symbol)

print(sum)
