single_string = input().split(", ")
for element in single_string:
    if element == "0":
        single_string.append(single_string.pop(single_string.index(element)))
for i in range(0, len(single_string)):
    single_string[i] = int(single_string[i])
print(single_string)