
import numpy as np

def solve_magic_square():
    grid = np.array([['x', 'x', 'x'], ['x', 'x', 'x'], ['x', 'x', 19]])
    numbers = list(range(12, 47))
    numbers.remove(19)  # remove the number already in the grid
    for num in numbers:
        if fill_grid(grid, num, numbers):
            return grid

def fill_grid(grid, num, numbers):
    for i in range(3):
        for j in range(3):
            if grid[i][j] == 'x':
                grid[i][j] = num
                numbers.remove(num)
                if check_conditions(grid):
                    return True
                else:
                    if fill_grid(grid, numbers[0], numbers):
                        return True
                    grid[i][j] = 'x'
                    numbers.append(num)
    return False

def check_conditions(grid):
    if np.sum(grid[1, :]) != 82 or np.sum(grid[:, 0]) != 71 or np.sum(grid.diagonal()[::-1]) != 70:
        return False
    return True

print(solve_magic_square())
