banned_words = input().split(", ")
text = input()

for w in banned_words:
    l = len(w)
    text = text.replace(w, "*" * l)

print(text)
