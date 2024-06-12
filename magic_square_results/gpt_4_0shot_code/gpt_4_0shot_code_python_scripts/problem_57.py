
import numpy as np

def solve_magic_square():
    grid = np.array([[42, 'x', 41, 'x'],
                     ['x', 48, 'x', 'x'],
                     ['x', 39, 30, 52],
                     ['x', 'x', 40, 'x']])
    row_sums = [None, 191, 157, None]
    col_sums = [None, 170, 162, None]
    diag_sum = 171
    numbers = set(range(28, 60)) - set(grid[grid != 'x'].astype(int))
    solutions = []

    def is_valid(i, j, num):
        old = grid[i, j]
        grid[i, j] = num
        valid = ((row_sums[i] is None or np.sum(grid[i, :][grid[i, :] != 'x']) <= row_sums[i]) and
                 (col_sums[j] is None or np.sum(grid[:, j][grid[:, j] != 'x']) <= col_sums[j]) and
                 (i != j or diag_sum is None or np.sum(grid.diagonal()[grid.diagonal() != 'x']) <= diag_sum))
        grid[i, j] = old
        return valid

    def solve():
        if len(numbers) == 0:
            return True
        for i in range(4):
            for j in range(4):
                if grid[i, j] == 'x':
                    for num in list(numbers):
                        if is_valid(i, j, num):
                            grid[i, j] = num
                            numbers.remove(num)
                            if solve():
                                solutions.append((i, j, num))
                                return True
                            grid[i, j] = 'x'
                            numbers.add(num)
                    return False
        return True

    solve()
    return solutions[::-1]

print(solve_magic_square())
