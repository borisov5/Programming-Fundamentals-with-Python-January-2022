food = float(input())
hay = float(input())
cover = float(input())
weight = float(input())
needs_enough = True
for day in range(1, 31):
    food -= 0.300
    if day % 2 == 0:
        hay -= (food * 0.05)
    if day % 3 == 0:
        cover -= (weight / 3)
    if food <= 0 or hay <= 0 or cover <= 0:
        needs_enough = False
        break

if needs_enough:
    print(f"Everything is fine! Puppy is happy! Food: {food:.2f}, Hay: {hay:.2f}, Cover: {cover:.2f}.")
else:
    print("Merry must go to the pet store!")
