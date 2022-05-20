rows_of_field = int(input())
rows = []
count_destroyed_ships = 0

for _ in range(rows_of_field):
    numbers = [int(num) for num in input().split(" ")]
    rows.append(numbers)

atacks = input().split(" ")

for i in range(len(atacks)):
    row, col = (atacks[i]).split("-")
    row = int(row)
    col = int(col)
    if rows[row][col] > 0:
        rows[row][col] -= 1
        if rows[row][col] == 0:
            count_destroyed_ships += 1

print(count_destroyed_ships)
