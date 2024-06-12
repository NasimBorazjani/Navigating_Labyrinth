
import numpy as np

def solve_magic_square(grid, numbers, row_sum, col_sum, diag_sum):
    if len(numbers) == 0:
        return grid

    for i in range(3):
        for j in range(3):
            if grid[i][j] == 'x':
                for num in numbers:
                    grid[i][j] = num
                    if check_valid(grid, row_sum, col_sum, diag_sum):
                        result = solve_magic_square(grid, [n for n in numbers if n != num], row_sum, col_sum, diag_sum)
                        if result is not None:
                            return result
                    grid[i][j] = 'x'
    return None

def check_valid(grid, row_sum, col_sum, diag_sum):
    for i in range(3):
        if 'x' not in grid[i] and sum(grid[i]) != row_sum[i]:
            return False
        if 'x' not in grid[:, i] and sum(grid[:, i]) != col_sum[i]:
            return False
    if 'x' not in np.diag(grid) and np.trace(grid) != diag_sum[0]:
        return False
    if 'x' not in np.diag(np.fliplr(grid)) and np.trace(np.fliplr(grid)) != diag_sum[1]:
        return False
    return True

grid = np.array([['x', 'x', 'x'], ['x', 'x', 'x'], [69, 71, 'x']])
numbers = [i for i in range(40, 90) if i not in [69, 71]]
row_sum = [152, 'x', 'x']
col_sum = [198, 'x', 'x']
diag_sum = ['x', 195]

solution = solve_magic_square(grid, numbers, row_sum, col_sum, diag_sum)
print(solution)
