number_snowballs = int(input())
snowball_value = 0
snowball_weight = 0
snowball_time = 0
snowball_quality = 0

for i in range(number_snowballs):
    weight = int(input())
    time = int(input())
    quality = int(input())
    value = (weight / time) ** quality
    if snowball_value < value:
        snowball_value = value
        snowball_weight = weight
        snowball_time = time
        snowball_quality = quality

print(f"{snowball_weight} : {snowball_time} = {int(snowball_value)} ({snowball_quality})")