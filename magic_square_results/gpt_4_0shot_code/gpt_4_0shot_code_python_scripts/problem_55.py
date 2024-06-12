
import numpy as np

def solve_magic_square(grid, row_sums, col_sums, diag_sum, used_numbers):
    for i in range(4):
        for j in range(4):
            if grid[i][j] == 'x':
                for num in range(28, 60):
                    if num not in used_numbers:
                        grid[i][j] = str(num)
                        used_numbers.add(num)
                        if check_constraints(grid, row_sums, col_sums, diag_sum):
                            if solve_magic_square(grid, row_sums, col_sums, diag_sum, used_numbers):
                                return True
                        grid[i][j] = 'x'
                        used_numbers.remove(num)
                return False
    return True

def check_constraints(grid, row_sums, col_sums, diag_sum):
    for i in range(4):
        if row_sums[i] is not None and sum(int(grid[i][j]) for j in range(4)) != row_sums[i]:
            return False
        if col_sums[i] is not None and sum(int(grid[j][i]) for j in range(4)) != col_sums[i]:
            return False
    if diag_sum is not None and sum(int(grid[i][3-i]) for i in range(4)) != diag_sum:
        return False
    return True

grid = np.array([['46', 'x', '58', '45'], ['x', 'x', '54', 'x'], ['x', 'x', 'x', 'x'], ['28', '53', '34', 'x']])
row_sums = [None, 168, 168, None]
col_sums = [None, 162, 195, None]
diag_sum = 168
used_numbers = set(int(grid[i][j]) for i in range(4) for j in range(4) if grid[i][j] != 'x')

if solve_magic_square(grid, row_sums, col_sums, diag_sum, used_numbers):
    solution = [(i, j, int(grid[i][j])) for i in range(4) for j in range(4) if grid[i][j] != 'x']
    print(solution)
else:
    print("No solution found")
