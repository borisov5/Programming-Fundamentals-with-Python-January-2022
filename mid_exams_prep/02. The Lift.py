people_waiting = int(input())
current_state = input().split(" ")
current_state = [int(wagon) for wagon in current_state]

for wagon in range(len(current_state)):
    empty_places = 4 - current_state[wagon]
    if empty_places == 0:
        continue
    elif 0 < empty_places <= 4:
        if people_waiting >= empty_places:
            people_waiting -= empty_places
            current_state[wagon] += empty_places
            empty_places = 0
        else:
            current_state[wagon] += people_waiting
            empty_places -= people_waiting
            people_waiting = 0

if people_waiting == 0 and empty_places > 0:
    print("The lift has empty spots!")
    print(" ".join(str(s) for s in current_state))
elif people_waiting > 0 and empty_places == 0:
    print(f"There isn't enough space! {people_waiting} people in a queue!")
    print(" ".join(str(s) for s in current_state))
else:
    print(" ".join(str(s) for s in current_state))
