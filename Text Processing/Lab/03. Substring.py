def substring(first, second):
    while first in second:
        second = second.replace(first, "")
    return second

key_word = input()
string = input()

print(substring(key_word, string))
