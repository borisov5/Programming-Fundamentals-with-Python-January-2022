list_of_numbers = input().split()
oposite_numbers = []
for index in range(len(list_of_numbers)):
    oposite_number = -int(list_of_numbers[index])
    oposite_numbers.append(oposite_number)
print(oposite_numbers)