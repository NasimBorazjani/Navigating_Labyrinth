
def find_empty_spot(puzzle):
    for i in range(3):
        for j in range(5):
            if puzzle[i][j] == '_':
                return i, j

def is_goal_state(puzzle):
    return all(puzzle[i][j] == i*5 + j + 1 for i in range(3) for j in range(5)) and puzzle[2][4] == '_'

def swap_tiles(puzzle, i1, j1, i2, j2):
    puzzle[i1][j1], puzzle[i2][j2] = puzzle[i2][j2], puzzle[i1][j1]

def solve_puzzle(puzzle):
    moves = []
    while not is_goal_state(puzzle):
        i, j = find_empty_spot(puzzle)
        if i == 2 and j == 4:
            if puzzle[2][3] != '_':
                swap_tiles(puzzle, 2, 4, 2, 3)
                moves.append(puzzle[2][3])
            else:
                swap_tiles(puzzle, 2, 4, 1, 4)
                moves.append(puzzle[1][4])
        elif i == 2:
            swap_tiles(puzzle, 2, 4, 2, 3)
            moves.append(puzzle[2][3])
        else:
            swap_tiles(puzzle, 2, 4, 1, 4)
            moves.append(puzzle[1][4])
    return moves

initial_state = [[42, 89, 21, 58, 67], [54, 32, 99, 69, 38], [77, 33, '_', 39, 16]]
solution = solve_puzzle(initial_state)
print(solution)
