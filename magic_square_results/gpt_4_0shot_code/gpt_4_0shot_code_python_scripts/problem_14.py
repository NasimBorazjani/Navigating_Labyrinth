
import numpy as np

def solve_magic_square():
    grid = np.array([['x', 32, 'x'], [38, 'x', 'x'], ['x', 'x', 'x']])
    numbers = set(range(28, 58)) - {32, 38}
    return solve(grid, numbers, [])

def solve(grid, numbers, solution):
    if len(numbers) == 0:
        if check_conditions(grid):
            return solution
        else:
            return None

    for number in list(numbers):
        for i in range(3):
            for j in range(3):
                if grid[i, j] == 'x':
                    grid[i, j] = number
                    solution.append((i, j, number))
                    numbers.remove(number)

                    result = solve(grid, numbers, solution)
                    if result is not None:
                        return result

                    grid[i, j] = 'x'
                    solution.remove((i, j, number))
                    numbers.add(number)

    return None

def check_conditions(grid):
    return np.sum(grid[1, :]) == 134 and np.sum(grid[:, 0]) == 143 and np.sum(grid.diagonal()[::-1]) == 131

print(solve_magic_square())
