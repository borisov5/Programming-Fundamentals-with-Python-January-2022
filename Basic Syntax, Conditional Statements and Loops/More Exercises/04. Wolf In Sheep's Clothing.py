string = input()
list = string.split(", ")
number = 0
for i in list:
    number += 1
    if i == "wolf":
        break
number = (len(list)) - number

if list[-1] == "wolf":
    print("Please go away and stop eating my sheep")
else:
    print(f"Oi! Sheep number {number}! You are about to be eaten by a wolf!")
