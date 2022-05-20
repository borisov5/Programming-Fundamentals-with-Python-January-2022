command = input().split(":")
dictionary = {}

while command[0] != "Results":
    if command[0] == "Add":
        person_name = command[1]
        health = command[2]
        energy = command[3]
        if person_name not in dictionary:
            dictionary[person_name] = {"Health": int(health), "Energy": int(energy)}
        else:
            dictionary[person_name]["Health"] += int(health)
    elif command[0] == "Attack":
        attacker_name = command[1]
        defender_name = command[2]
        damage = int(command[3])
        if (attacker_name in dictionary) and (defender_name in dictionary):
            dictionary[defender_name]["Health"] -= damage
            dictionary[attacker_name]["Energy"] -= 1
        if dictionary[defender_name]["Health"] <= 0:
            del dictionary[defender_name]
            print(f"{defender_name} was disqualified!")
        if dictionary[attacker_name]["Energy"] <= 0:
            del dictionary[attacker_name]
            print(f"{attacker_name} was disqualified!")
    elif command[0] == "Delete":
        username = command[1]
        if username == "All":
            dictionary.clear()
        else:
            del dictionary[username]

    command = input().split(":")

people_count = 0
for key in dictionary.keys():
    people_count += 1
if people_count != 0:
    print(f"People count: {people_count}")

for key, values in dictionary.items():
    print(f"{key} - {values['Health']} - {values['Energy']}")
