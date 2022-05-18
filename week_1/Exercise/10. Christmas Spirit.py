quantity = int(input())
days = int(input())
budget = 0
total_spirit = 0

ornament_set = 2
tree_skirt = 5
tree_garlands = 3
tree_lights = 15

for i in range(1, days + 1):
    if (i % 11) == 0:
        quantity += 2

    if (i % 2) == 0:
        budget += (quantity * ornament_set)
        total_spirit += 5

    if (i % 3) == 0:
        budget += (quantity * (tree_skirt + tree_garlands))
        total_spirit += 13

    if (i % 5) == 0:
        budget += (tree_lights * quantity)
        total_spirit += 17
        if (i % 3) == 0:
            total_spirit += 30

    if (i % 10) == 0:
        budget += (tree_skirt + tree_garlands + tree_lights)
        total_spirit -= 20

if (days % 10) == 0:
    total_spirit -= 30

print(f"Total cost: {budget}")
print(f"Total spirit: {total_spirit}")