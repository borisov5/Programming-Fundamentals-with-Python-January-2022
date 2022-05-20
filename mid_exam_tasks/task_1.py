needed_experience = float(input())
count_of_battles = int(input())

for battle_num in range(1, count_of_battles + 1):
    experience_earned = float(input())
    if battle_num % 3 == 0:
        experience_earned *= 1.15
    if battle_num % 5 == 0:
        experience_earned *= 0.90
    if battle_num % 15 == 0:
        experience_earned *= 1.05
    needed_experience -= experience_earned
    if needed_experience <= 0:
        break

if needed_experience <= 0:
    print(f"Player successfully collected his needed experience for {battle_num} battles.")
else:
    print(f"Player was not able to collect the needed experience, {needed_experience:.2f} more needed.")
