
import numpy as np

def solve_magic_square():
    grid = np.array([['x', 'x', 'x'], ['x', 'x', 55], ['x', 'x', 'x']])
    numbers = list(range(48, 78))
    numbers.remove(55)
    return solve(grid, numbers, [])

def solve(grid, numbers, result):
    if not numbers:
        if check_conditions(grid):
            return result
        else:
            return None
    else:
        for i in range(3):
            for j in range(3):
                if grid[i][j] == 'x':
                    for number in numbers:
                        grid[i][j] = number
                        new_result = result + [(i, j, number)]
                        new_numbers = numbers.copy()
                        new_numbers.remove(number)
                        solution = solve(grid, new_numbers, new_result)
                        if solution is not None:
                            return solution
                        grid[i][j] = 'x'
        return None

def check_conditions(grid):
    return np.sum(grid[:, 0]) == 190 and np.sum(grid[1, :]) == 167 and np.sum(grid.diagonal()[::-1]) == 172

print(solve_magic_square())
