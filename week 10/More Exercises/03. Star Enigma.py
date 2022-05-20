import re

number = int(input())
attacked_planets = []
destroyed_planets = []
attacked_planets_count = 0
destroyed_planets_count = 0
for _ in range(number):
    message = input()
    decrypted_message = ""
    attack_type = ""
    planet_name = ""
    planet_population = 0
    soldier_count = 0
    key = 0

    for symbol in message:
        if symbol in ["S", "T", "A", "R", "s", "t", "a", "r"]:
            key += 1

    for symbol in message:
        decrypted_message += chr(ord(symbol) - key)

    matches = re.finditer(r".*@([A-Za-z]+).*:(\d+).*!(A|D)!.*->(\d+)", decrypted_message)
    for match in matches:
        planet_name = match.group(1)
        planet_population = int(match.group(2))
        attack_type = match.group(3)
        soldier_count = int(match.group(4))

    if attack_type == "A":
        attacked_planets.append(planet_name)
        attacked_planets_count += 1
    elif attack_type == "D":
        destroyed_planets.append(planet_name)
        destroyed_planets_count += 1

sorted_attacked_planets = sorted(attacked_planets)
sorted_destroyed_planets = sorted(destroyed_planets)
print(f"Attacked planets: {attacked_planets_count}")
for planet in sorted_attacked_planets:
    print(f"-> {planet}")
print(f"Destroyed planets: {destroyed_planets_count}")
for planet in sorted_destroyed_planets:
    print(f"-> {planet}")
