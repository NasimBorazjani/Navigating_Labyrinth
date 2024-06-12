
import numpy as np

def is_valid(grid, rows, cols, diag):
    for i in range(4):
        if rows[i] is not None and np.sum(grid[i, :]) != rows[i]:
            return False
        if cols[i] is not None and np.sum(grid[:, i]) != cols[i]:
            return False
    if diag is not None and np.sum(grid.diagonal()) != diag:
        return False
    return True

def solve(grid, rows, cols, diag, nums):
    if len(nums) == 0:
        return grid
    for i in range(4):
        for j in range(4):
            if grid[i, j] == 'x':
                for num in nums:
                    grid[i, j] = num
                    if is_valid(grid, rows, cols, diag):
                        result = solve(grid, rows, cols, diag, [n for n in nums if n != num])
                        if result is not None:
                            return result
                    grid[i, j] = 'x'
                return None

grid = np.array([['x', 41, 67, 'x'],
                 ['x', 73, 'x', 91],
                 ['x', 43, 'x', 76],
                 [80, 'x', 'x', 86]], dtype=object)

rows = [None, 298, 222, None]
cols = [None, 240, 266, None]
diag = 299
nums = [i for i in range(41, 93) if i not in grid]

solution = solve(grid, rows, cols, diag, nums)

result = []
for i in range(4):
    for j in range(4):
        if isinstance(solution[i, j], int):
            result.append((i, j, solution[i, j]))

print(result)
