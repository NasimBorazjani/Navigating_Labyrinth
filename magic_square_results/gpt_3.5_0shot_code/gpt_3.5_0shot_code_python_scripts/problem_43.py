
from itertools import permutations

def check_sums(grid):
    row_sums = [180, 202]
    col_sums = [212, 185]
    diag_sum = 193

    for i in range(2):
        if sum(grid[i]) != row_sums[i]:
            return False

    for j in range(2):
        col_sum = sum(grid[i][j] for i in range(4))
        if col_sum != col_sums[j]:
            return False

    if sum(grid[i][i] for i in range(4)) != diag_sum:
        return False

    if sum(grid[i][3-i] for i in range(4)) != diag_sum:
        return False

    return True

def solve_magic_square():
    grid = [['x', '51', '39', 'x'],
            ['x', 'x', '48', '37'],
            ['54', 'x', 'x', 'x'],
            ['x', 'x', 'x', '53']]

    unknown_positions = [(i, j) for i in range(4) for j in range(4) if grid[i][j] == 'x']
    possible_values = [x for x in range(35, 62)]

    for perm in permutations(possible_values, len(unknown_positions)):
        for idx, (i, j) in enumerate(unknown_positions):
            grid[i][j] = perm[idx]

        if check_sums(grid):
            solution = [(i, j, grid[i][j]) for i, j in unknown_positions]
            return solution

    return None

solution = solve_magic_square()
print(solution)
