
import numpy as np

def solve_magic_square(grid, row_sum, col_sum, diag_sum, used, row=0, col=0):
    if row == 3:
        return True
    next_row, next_col = (row, col + 1) if col != 2 else (row + 1, 0)
    if grid[row][col] != 'x':
        return solve_magic_square(grid, row_sum, col_sum, diag_sum, used, next_row, next_col)
    for num in range(40, 90):
        if used[num - 40]:
            continue
        grid[row][col] = str(num)
        row_sum[row] += num
        col_sum[col] += num
        if row == col:
            diag_sum[0] += num
        if row + col == 2:
            diag_sum[1] += num
        if row_sum[row] <= 209 and col_sum[col] <= 150 and diag_sum[0] <= 169 and diag_sum[1] <= 169:
            used[num - 40] = True
            if solve_magic_square(grid, row_sum, col_sum, diag_sum, used, next_row, next_col):
                return True
            used[num - 40] = False
        grid[row][col] = 'x'
        row_sum[row] -= num
        col_sum[col] -= num
        if row == col:
            diag_sum[0] -= num
        if row + col == 2:
            diag_sum[1] -= num
    return False

grid = np.array([['48', 'x', 'x'], ['x', 'x', 'x'], ['x', '49', 'x']])
row_sum = [int(grid[i][j]) if grid[i][j] != 'x' else 0 for i in range(3) for j in range(3) if i == j]
col_sum = [int(grid[j][i]) if grid[j][i] != 'x' else 0 for i in range(3) for j in range(3) if i == j]
diag_sum = [int(grid[i][2 - i]) if grid[i][2 - i] != 'x' else 0 for i in range(3)]
used = [False] * 50
solve_magic_square(grid, row_sum, col_sum, diag_sum, used)
solution = [(i, j, int(grid[i][j])) for i in range(3) for j in range(3) if grid[i][j] != 'x']
print(solution)
