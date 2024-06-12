
from itertools import permutations

def check_sums(grid):
    row_sums = [None, 72, 97, None]
    col_sums = [None, 102, 100, None]
    diag_sum = 46

    for i in range(4):
        row_sum = sum([int(x) if x != 'x' else 0 for x in grid[i]])
        if row_sums[i] is not None and row_sum != row_sums[i]:
            return False

        col_sum = sum([int(grid[j][i]) if grid[j][i] != 'x' else 0 for j in range(4)])
        if col_sums[i] is not None and col_sum != col_sums[i]:
            return False

    diag_sum_check = int(grid[0][3]) + int(grid[1][2]) + int(grid[2][1]) + int(grid[3][0])
    if diag_sum_check != diag_sum:
        return False

    return True

grid = [['x', 'x', '27', '9'],
        ['21', 'x', 'x', '15'],
        ['x', '16', '31', 'x'],
        ['11', 'x', '32', 'x']]

possible_values = [str(i) for i in range(9, 41)]
unknown_positions = [(i, j) for i in range(4) for j in range(4) if grid[i][j] == 'x']

min_sum = float('inf')
min_solution = None

for perm in permutations(possible_values, len(unknown_positions)):
    temp_grid = [row.copy() for row in grid]
    for pos, val in zip(unknown_positions, perm):
        temp_grid[pos[0]][pos[1]] = val

    if check_sums(temp_grid):
        total_sum = sum([int(val) for row in temp_grid for val in row if val != 'x'])
        if total_sum < min_sum:
            min_sum = total_sum
            min_solution = [(pos[0], pos[1], int(val)) for pos, val in zip(unknown_positions, perm)]

print(min_solution)
