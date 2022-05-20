names = input().split(" ")
number = int(input())

for _ in range(number):
    command = input().split(" ")
    if command[0] == "Include":
        coffee = command[1]
        names.append(coffee)
    elif command[0] == "Remove":
        first_last = command[1]
        number_of_coffees = int(command[2])
        if first_last == "first":
            if number_of_coffees < len(names):
                for i in range(number_of_coffees):
                    names.pop(0)
        elif first_last == "last":
            if number_of_coffees < len(names):
                for i in range(number_of_coffees):
                    names.pop()
    elif command[0] == "Prefer":
        coffee_index_one = int(command[1])
        coffee_index_two = int(command[2])
        if 0 <= coffee_index_one < len(names) and 0 <= coffee_index_two < len(names):
            if coffee_index_one < coffee_index_two:
                coffee_two = names.pop(coffee_index_two)
                coffee_one = names.pop(coffee_index_one)
                names.insert(coffee_index_one, coffee_two)
                names.insert(coffee_index_two, coffee_one)
            else:
                coffee_one = names.pop(coffee_index_one)
                coffee_two = names.pop(coffee_index_two)
                names.insert(coffee_index_two, coffee_one)
                names.insert(coffee_index_one, coffee_two)
    elif command[0] == "Reverse":
        names.reverse()

print("Coffees:")
print(" ".join(names))
