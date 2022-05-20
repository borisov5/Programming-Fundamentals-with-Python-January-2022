def check_if_she_cant_get_out(starting_row, starting_col, maze):
    if maze[starting_row][starting_col] == '#':
        print('Kate cannot get out')


def check_if_she_got_out(k_row, k_col, previous_positions):
    if k_row == len(maze) - 1 or k_row == 0 or k_col == len(maze[0]) - 1 or k_col == 0:
        print(f'Kate got out in {len(previous_positions) + 1} moves')
        return True
    return False


def get_next_position(k_row, k_col, maze):
    if maze[k_row - 1][k_col] == ' ' and [k_row - 1, k_col] not in previous_positions:
        previous_positions.append([k_row, k_col])
        k_row -= 1
    elif maze[k_row + 1][k_col] == ' ' and [k_row + 1, k_col] not in previous_positions:
        previous_positions.append([k_row, k_col])
        k_row += 1
    elif maze[k_row][k_col - 1] == ' ' and [k_row, k_col - 1] not in previous_positions:
        previous_positions.append([k_row, k_col])
        k_col -= 1
    elif maze[k_row][k_col + 1] == ' ' and [k_row, k_col + 1] not in previous_positions:
        previous_positions.append([k_row, k_col])
        k_col += 1
    else:
        maze[k_row][k_col] = '#'
        previous_positions.clear()
        k_row, k_col = starting_row, starting_col

    return k_row, k_col


def create_maze(size):
    maze = []
    kate_row, kate_col = None, None

    for _ in range(size):
        maze.append([el for el in input()])
    for row in maze:
        if 'k' in row:
            kate_row, kate_col = maze.index(row), row.index('k')
            break

    return maze, kate_row, kate_col


size = int(input())
maze, starting_row, starting_col = create_maze(size)

kate_row, kate_col = starting_row, starting_col
previous_positions = []
go_out = False

while maze[starting_row][starting_col] == 'k':
    check_if_she_got_out(starting_row, starting_col, maze)
    kate_row, kate_col = get_next_position(kate_row, kate_col, maze)
    go_out = check_if_she_cant_get_out(kate_row, kate_col, previous_positions)
    if got_out:
        break

if not go_out:
    print('Kate cannot get out')
    