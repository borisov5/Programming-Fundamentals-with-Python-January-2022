command = input()
input_args = []
dictionary = {}

while command != "stop":
    input_args.append(command)
    command = input()

for i in range(0, len(input_args), 2):
    product = input_args[i]
    quantity = int(input_args[i + 1])
    if product in dictionary.keys():
        dictionary[product] += quantity
    else:
        dictionary[product] = quantity

for key, value in dictionary.items():
    print(f"{key} -> {value}")
