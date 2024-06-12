
import numpy as np

def solve_magic_square():
    grid = np.array([['x', 'x', 80, 72],
                     [44, 'x', 39, 'x'],
                     ['x', 70, 64, 'x'],
                     ['x', 67, 'x', 42]])

    row_sums = [None, 221, 257, None]
    col_sums = [None, 252, 238, None]
    diag_sum = 221

    numbers = set(range(37, 84))
    for row in grid:
        for num in row:
            if num != 'x':
                numbers.remove(num)

    def check_constraints(grid, row_sums, col_sums, diag_sum):
        for i in range(4):
            if row_sums[i] is not None and np.sum(grid[i, :]) != row_sums[i]:
                return False
            if col_sums[i] is not None and np.sum(grid[:, i]) != col_sums[i]:
                return False
        if diag_sum is not None and np.sum(grid.diagonal()) != diag_sum:
            return False
        return True

    def solve(grid, numbers):
        for i in range(4):
            for j in range(4):
                if grid[i, j] == 'x':
                    for num in numbers:
                        grid[i, j] = num
                        if check_constraints(grid, row_sums, col_sums, diag_sum):
                            if solve(grid, numbers - {num}):
                                return True
                        grid[i, j] = 'x'
                    return False
        return True

    if solve(grid, numbers):
        solution = []
        for i in range(4):
            for j in range(4):
                if type(grid[i, j]) == int:
                    solution.append((i, j, grid[i, j]))
        return solution

print(solve_magic_square())
