health = 100
bitcoins = 0
dungeon_rooms = input().split("|")
im_alive = True
counter = 1
for room in dungeon_rooms:
    room = room.split(" ")
    command = room[0]
    if command == "potion":
        amount = int(room[1])
        health += amount
        if health > 100:
            amount -= (health - 100)
            health = 100
        print(f"You healed for {amount} hp.")
        print(f"Current health: {health} hp.")
    elif command == "chest":
        amount = int(room[1])
        bitcoins += amount
        print(f"You found {amount} bitcoins.")
    else:
        monster = room[0]
        monster_atack = int(room[1])
        health -= monster_atack
        if health > 0:
            print(f"You slayed {monster}.")
        else:
            im_alive = False
            print(f"You died! Killed by {monster}.")
            print(f"Best room: {counter}")
            break
    counter += 1

if im_alive:
    print("You've made it!")
    print(f"Bitcoins: {bitcoins}")
    print(f"Health: {health}")
