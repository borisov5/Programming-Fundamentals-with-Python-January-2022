string = input()
numbers_list = []
non_numbers = []
take_list = []
skip_list = []
final_string = ""

for symbol in string:
    if symbol.isdigit():
        numbers_list.append(symbol)
    else:
        non_numbers.append(symbol)

for num in range(len(numbers_list)):
    if num % 2 == 0:
        take_list.append(numbers_list[num])
    else:
        skip_list.append(numbers_list[num])

take_list = [int(num) for num in take_list]
skip_list = [int(num) for num in skip_list]
counter = 0
list_index = 0

while len(non_numbers) > 0:

    counter = take_list[list_index]
    if counter != 0:
        for i in range(counter):
            final_string += non_numbers[0]
            non_numbers.remove(non_numbers[0])
            if len(non_numbers) == 0:
                break
    if len(non_numbers) == 0:
        break
    counter = 0
    counter = skip_list[list_index]
    if counter != 0:
        for i in range(counter):
            non_numbers.remove(non_numbers[0])
            if len(non_numbers) == 0:
                break
    counter = 0
    list_index += 1
    if list_index == len(take_list):
        break

print(final_string)
