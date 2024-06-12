
import numpy as np

def solve_magic_square():
    grid = np.array([[47, 'x', 'x'], ['x', 'x', 'x'], ['x', 'x', 'x']])
    numbers = list(range(26, 66))
    numbers.remove(47)  # remove the number already in the grid
    return solve(grid, numbers, [])

def solve(grid, numbers, solution):
    if 'x' not in grid:
        if check_conditions(grid):
            return solution
        else:
            return None
    else:
        for i in range(3):
            for j in range(3):
                if grid[i][j] == 'x':
                    for num in numbers:
                        grid[i][j] = num
                        solution.append((i, j, num))
                        numbers.remove(num)
                        result = solve(grid, numbers, solution)
                        if result is not None:
                            return result
                        grid[i][j] = 'x'
                        solution.remove((i, j, num))
                        numbers.append(num)
        return None

def check_conditions(grid):
    return np.sum(grid[:, 0]) == 93 and np.sum(grid[1, :]) == 135 and np.sum(grid.diagonal()[::-1]) == 106

print(solve_magic_square())
