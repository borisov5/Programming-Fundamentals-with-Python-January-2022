import re

participants = input().split(", ")
participants_score = {}
for participant in participants:
    participants_score[participant] = 0

command = input()
while command != "end of race":
    name_pattern = re.findall(r"[A-Za-z]+", command)
    kilometers_pattern = re.findall(r"[0-9]", command)
    name = "".join(name_pattern)
    kilometers = 0
    for digit in kilometers_pattern:
        kilometers += int(digit)
    if name in participants_score:
        participants_score[name] += kilometers
    command = input()

sorted_participants = sorted(participants_score.items(), key=lambda kvpt: kvpt[1], reverse=True)
print(f"1st place: {sorted_participants[0][0]}")
print(f"2nd place: {sorted_participants[1][0]}")
print(f"3rd place: {sorted_participants[2][0]}")
