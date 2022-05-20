sequence = input().split()
sequence = [int(num) for num in sequence]
sorted_sequence = sorted(sequence, reverse=True)
average_value = 0
numbers = 0
top_five = []
for num in sequence:
    average_value += int(num)
    numbers += 1
average_value /= numbers

for number in sorted_sequence:
    if number > average_value:
        top_five.append(number)
    if len(top_five) == 5:
        break

if len(top_five) == 0:
    print("No")
else:
    for number in top_five:
        print(number, end=" ")
