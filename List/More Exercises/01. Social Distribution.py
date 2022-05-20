population = [int(population) for population in input().split(", ")]
min_wealth = int(input())
max_wealth = 0
index_max_wealth = 0
possible_distribution = True

for index in range(0, len(population)):

    for max_index in range(0, len(population)):
        if population[max_index] > max_wealth:
            max_wealth = population[max_index]
            index_max_wealth = max_index

    if population[index] < min_wealth:
        difference = min_wealth - population[index]
        if population[index_max_wealth] - difference < min_wealth:
            print("No equal distribution possible")
            possible_distribution = False
            break
        else:
            population[index_max_wealth] -= difference
            population[index] += difference
    max_wealth = 0
    index_max_wealth = 0

if possible_distribution:
    print(population)
