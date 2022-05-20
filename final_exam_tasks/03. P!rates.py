class City:
    def __init__(self, name, population, gold):
        self.name = name
        self.population = population
        self.gold = gold

    def plunder(name, people, gold):
        cities[city]['population'] -= people
        cities[city]['gold'] -= gold
        if cities[city]['population'] <= 0 or cities[city]['gold'] <= 0:
            del cities[city]
            return f"{name} plundered! {gold} gold stolen, {people} citizens killed.\n{name} has been wiped off the map!"
        return f"{name} plundered! {gold} gold stolen, {people} citizens killed."

    def prosper(self):
        pass


cities = {}

while True:
    command = input()
    if command == "Sail":
        break
    city_name, population, gold = command.split("||")
    cities[city_name] = City(city_name, int(population), int(gold))

while True:
    action = input().split("=>")
    if action[0] == "End":
        break
    elif action[0] == "Plunder":
        town = action[1]
        humans = int(action[2])
        amount_gold = int(action[3])
        result = plunder(town, humans, amount_gold)
        print(result)
    elif action[0] == "Prosper":
        town = action[1]
        amount_gold = int(action[2])
        result = City.prosper(town, amount_gold)
        print(result)

