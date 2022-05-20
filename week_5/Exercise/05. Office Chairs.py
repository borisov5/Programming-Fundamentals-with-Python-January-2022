number_of_rooms = int(input())
total_free_chairs = 0
enough_chairs = True
for room in range(1, number_of_rooms + 1):
    chairs_args = input().split(" ")
    chairs = len(chairs_args[0])
    visitors = int(chairs_args[1])
    result = visitors - chairs
    if result > 0:
        print(f"{result} more chairs needed in room {room}")
        enough_chairs = False
    elif result < 0:
        total_free_chairs += result

if enough_chairs:
    if total_free_chairs <= 0:
        print(f"Game On, {abs(total_free_chairs)} free chairs left")
