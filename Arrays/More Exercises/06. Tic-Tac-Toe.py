first_row = input().split(" ")
second_row = input().split(" ")
third_row = input().split(" ")
first_column = list(first_row[0] + second_row[0] + third_row[0])
second_column = list(first_row[1] + second_row[1] + third_row[1])
third_column = list(first_row[2] + second_row[2] + third_row[2])
diagonal_one = list(first_row[0] + second_row[1] + third_row[2])
diagonal_two = list(first_row[2] + second_row[1] + third_row[0])
win_the_game = False
player = ""
list = [first_row, second_row, third_row, first_column,
        second_column, third_column, diagonal_one, diagonal_two]

for index in list:
    if set(index) == {'1'}:
        win_the_game = True
        player = "First"
        break
    elif set(index) == {'2'}:
        win_the_game = True
        player = "Second"
        break

if win_the_game:
    print(f"{player} player won")
else:
    print("Draw!")
