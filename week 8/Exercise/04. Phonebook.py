phonebook = {}
entry = input().split("-")
searches = 0
while True:
    if entry[0].isalpha() is False:
        searches += int(entry[0])
        break
    name = entry[0]
    number = entry[1]
    phonebook[name] = number
    entry = input().split("-")

for search in range(searches):
    name = str(input())
    if name in phonebook.keys():
        print(f"{name} -> {phonebook[name]}")
    else:
        print(f"Contact {name} does not exist.")
