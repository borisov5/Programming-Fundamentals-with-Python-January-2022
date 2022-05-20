text = input()
counter = -1
list = []
for i in text:
    i = ord(i)
    counter += 1
    if i in range(65, 91):
        list.append(counter)
print(list)