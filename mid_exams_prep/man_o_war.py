pirate_ship = list(map(int, input().split('>')))
warship = list(map(int, input().split('>')))
capacity = int(input())
command = input().split(" ")
pirate_ship_sinks = False

while command[0] != "Retire":
    if command[0] == "Fire":
        index = int(command[1])
        damage = int(command[2])
        if 0 <= index < len(warship):
            warship[index] -= damage
            if warship[index] <= 0:
                print("You won! The enemy ship has sunken.")
                pirate_ship_sinks = True
                break
    elif command[0] == "Defend":
        start_index = int(command[1])
        end_index = int(command[2])
        damage = int(command[3])
        if (0 <= start_index < len(pirate_ship)) and (0 <= end_index < len(pirate_ship)):
            for index in range(start_index, end_index + 1):
                pirate_ship[index] -= damage
                if pirate_ship[index] <= 0:
                    print(f"You lost! The pirate ship has sunken.")
                    pirate_ship_sinks = True
                    break
            if pirate_ship_sinks:
                break
    elif command[0] == "Repair":
        index = int(command[1])
        health = int(command[2])
        if 0 <= index < len(pirate_ship):
            if pirate_ship[index] + health > capacity:
                health = capacity - pirate_ship[index]
            pirate_ship[index] += health
    elif command[0] == "Status":
        min_capacity = capacity * 0.2
        count = len([x for x in pirate_ship if x < min_capacity])
        print(f"{count} sections need repair.")
    command = input().split(" ")

if not pirate_ship_sinks:
    print(f"Pirate ship status: {sum(pirate_ship)}")
    print(f"Warship status: {sum(warship)}")
