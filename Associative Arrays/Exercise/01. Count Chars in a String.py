strings = input().split(" ")
dictionary = {}

for string in strings:

    for index in string:
        if index not in dictionary.keys():
            char = index
            occurrences = 1
            dictionary[char] = occurrences
        else:
            dictionary[index] += 1

for key, value in dictionary.items():
    print(f"{key} -> {value}")
