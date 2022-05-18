command = input()
coffee_number = 0
while True:
    if command == "coding" or command == "dog" or command == "cat" or command == "movie":
        coffee_number += 1
    elif command == "CODING" or command == "DOG" or command == "CAT" or command == "MOVIE":
        coffee_number += 2
    elif command == "END":
        break
    command = input()

if coffee_number > 5:
    print("You need extra sleep")
else:
    print(coffee_number)
