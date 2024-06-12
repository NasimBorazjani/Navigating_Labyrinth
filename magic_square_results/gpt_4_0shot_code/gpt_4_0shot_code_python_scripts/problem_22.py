
import numpy as np

def solve_magic_square():
    grid = np.array([['x', 'x', 'x'], ['x', 'x', 'x'], ['x', '43', 'x']])
    numbers = list(range(12, 47))
    numbers.remove(43)
    for num in numbers:
        if fill_grid(grid, num, numbers):
            return grid

def fill_grid(grid, num, numbers):
    if np.count_nonzero(grid == 'x') == 0:
        return check_conditions(grid)
    for i in range(3):
        for j in range(3):
            if grid[i][j] == 'x':
                grid[i][j] = num
                numbers.remove(num)
                if check_conditions(grid):
                    if fill_grid(grid, numbers[0], numbers):
                        return True
                grid[i][j] = 'x'
                numbers.append(num)
    return False

def check_conditions(grid):
    if np.count_nonzero(grid == 'x') == 0:
        if grid.sum(axis=0)[0] == 120 and grid.sum(axis=1)[1] == 105 and np.fliplr(grid).diagonal().sum() == 99:
            return True
    return False

grid = solve_magic_square()
result = []
for i in range(3):
    for j in range(3):
        if grid[i][j] != 'x':
            result.append((i, j, grid[i][j]))
print(result)
