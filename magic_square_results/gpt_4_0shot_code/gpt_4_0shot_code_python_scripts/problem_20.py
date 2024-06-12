
import numpy as np

def solve_magic_square(grid, numbers, sums):
    if len(numbers) == 0:
        return grid

    for i in range(3):
        for j in range(3):
            if grid[i][j] == 'x':
                for num in numbers:
                    grid[i][j] = str(num)
                    if check_sums(grid, sums):
                        result = solve_magic_square(grid, [n for n in numbers if n != num], sums)
                        if result is not None:
                            return result
                    grid[i][j] = 'x'
    return None

def check_sums(grid, sums):
    for i in range(3):
        if 'x' not in grid[i] and sum(int(n) for n in grid[i]) != sums['row'][i]:
            return False
        if 'x' not in grid[:, i] and sum(int(n) for n in grid[:, i]) != sums['col'][i]:
            return False
    if 'x' not in np.diag(np.fliplr(grid)) and sum(int(n) for n in np.diag(np.fliplr(grid))) != sums['diag']:
        return False
    return True

grid = np.array([['62', '82', 'x'], ['x', 'x', 'x'], ['x', 'x', 'x']])
numbers = [i for i in range(50, 85) if str(i) not in grid.flatten()]
sums = {'row': [None, 207, None], 'col': [233, None, None], 'diag': 185}

solution = solve_magic_square(grid, numbers, sums)
print(solution)
