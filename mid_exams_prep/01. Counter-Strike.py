initial_energy = int(input())
not_out_of_energy = True
won_battles = 0
distance = input()
while distance != "End of battle":
    if initial_energy <= 0 or int(distance) > initial_energy:
        print(f"Not enough energy! Game ends with {won_battles} won battles and {initial_energy} energy")
        not_out_of_energy = False
        break
    initial_energy -= int(distance)
    won_battles += 1
    if won_battles % 3 == 0:
        initial_energy += won_battles
    distance = input()

if not_out_of_energy:
    print(f"Won battles: {won_battles}. Energy left: {initial_energy}")
