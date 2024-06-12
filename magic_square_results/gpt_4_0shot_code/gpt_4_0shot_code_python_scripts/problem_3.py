
import numpy as np

def solve_magic_square(grid, numbers, row_sum, col_sum, diag_sum):
    if len(numbers) == 0:
        return grid

    for i in range(3):
        for j in range(3):
            if grid[i][j] == 'x':
                for num in numbers:
                    grid[i][j] = str(num)
                    if check_valid(grid, row_sum, col_sum, diag_sum):
                        result = solve_magic_square(grid, [n for n in numbers if n != num], row_sum, col_sum, diag_sum)
                        if result is not None:
                            return result
                    grid[i][j] = 'x'
    return None

def check_valid(grid, row_sum, col_sum, diag_sum):
    for i in range(3):
        if 'x' not in grid[i] and sum(int(x) for x in grid[i]) != row_sum[i]:
            return False
        if 'x' not in grid[:, i] and sum(int(x) for x in grid[:, i]) != col_sum[i]:
            return False
    if 'x' not in np.diag(np.fliplr(grid)) and sum(int(x) for x in np.diag(np.fliplr(grid))) != diag_sum:
        return False
    return True

grid = np.array([['25', 'x', 'x'], ['x', 'x', 'x'], ['x', 'x', 'x']])
numbers = list(range(20, 40))
numbers.remove(25)
row_sum = [None, 86, None]
col_sum = [99, None, None]
diag_sum = 76

solution = solve_magic_square(grid, numbers, row_sum, col_sum, diag_sum)
print(solution)
