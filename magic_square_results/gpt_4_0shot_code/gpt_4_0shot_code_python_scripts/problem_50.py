
import numpy as np

def solve_magic_square(grid, row_sums, col_sums, diag_sum, used, row=0, col=0):
    if row == 4:
        return True
    if grid[row][col] != 'x':
        if solve_magic_square(grid, row_sums, col_sums, diag_sum, used, row + (col + 1) // 4, (col + 1) % 4):
            return True
    else:
        for num in range(9, 41):
            if used[num - 9]:
                continue
            grid[row][col] = num
            used[num - 9] = True
            if (row_sums[row] is None or np.sum(grid[row]) <= row_sums[row]) and \
               (col_sums[col] is None or np.sum(grid[:, col]) <= col_sums[col]) and \
               (row != col or np.trace(np.fliplr(grid)) <= diag_sum):
                if solve_magic_square(grid, row_sums, col_sums, diag_sum, used, row + (col + 1) // 4, (col + 1) % 4):
                    return True
            grid[row][col] = 'x'
            used[num - 9] = False
    return False

grid = np.array([['x', 'x', 'x', 39],
                 [28, 'x', 'x', 'x'],
                 ['x', 11, 33, 'x'],
                 [18, 20, 38, 35]], dtype=object)
row_sums = [None, 114, 84, None]
col_sums = [None, 77, 110, None]
diag_sum = 98
used = [False] * 32
solve_magic_square(grid, row_sums, col_sums, diag_sum, used)

solution = [(i, j, grid[i][j]) for i in range(4) for j in range(4) if type(grid[i][j]) is int]
print(solution)
