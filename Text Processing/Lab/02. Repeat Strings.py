words = input().split()
res = []

for word in words:
    length = len(word)
    multiplied_word = word * length

    res.append(multiplied_word)

print("".join(res))
