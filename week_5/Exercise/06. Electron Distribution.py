number_of_electrons = int(input())
electrons = []
number = 1
while number_of_electrons > 0:
    electron = 2 * number * number
    if electron > number_of_electrons:
        electrons.append(number_of_electrons)
        break
    electrons.append(electron)
    number += 1
    number_of_electrons -= electron

print(electrons)