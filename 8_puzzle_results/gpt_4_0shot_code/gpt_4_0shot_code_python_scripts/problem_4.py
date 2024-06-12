
def find_empty(puzzle):
    for i in range(3):
        for j in range(3):
            if puzzle[i][j] == '_':
                return i, j

def find_swappable(puzzle, empty_i, empty_j):
    swappable = []
    if empty_i > 0:
        swappable.append((empty_i - 1, empty_j))
    if empty_i < 2:
        swappable.append((empty_i + 1, empty_j))
    if empty_j > 0:
        swappable.append((empty_i, empty_j - 1))
    if empty_j < 2:
        swappable.append((empty_i, empty_j + 1))
    return swappable

def solve_puzzle(puzzle):
    solution = []
    while puzzle != [[89, 83, 71], [70, 66, 42], [25, 24, '_']]:
        empty_i, empty_j = find_empty(puzzle)
        swappable = find_swappable(puzzle, empty_i, empty_j)
        max_tile = max(swappable, key=lambda x: puzzle[x[0]][x[1]])
        solution.append(puzzle[max_tile[0]][max_tile[1]])
        puzzle[empty_i][empty_j], puzzle[max_tile[0]][max_tile[1]] = puzzle[max_tile[0]][max_tile[1]], puzzle[empty_i][empty_j]
    return solution

puzzle = [[66, 89, 70], [25, 42, 83], ['_', 24, 71]]
print(solve_puzzle(puzzle))
