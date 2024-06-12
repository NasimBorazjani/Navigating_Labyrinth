
import numpy as np

def solve(grid, numbers, sum_elements):
    if len(numbers) == 0:
        return True, sum_elements

    min_sum = float('inf')
    solution = None
    for number in numbers:
        for i in range(3):
            for j in range(3):
                if grid[i][j] == 'x' and is_valid(grid, i, j, number):
                    grid[i][j] = number
                    new_sum_elements = sum_elements.copy()
                    if i == 0 or j == 2 or i == j:
                        new_sum_elements.append(number)
                    new_numbers = numbers.copy()
                    new_numbers.remove(number)
                    if solve(grid, new_numbers, new_sum_elements):
                        current_sum = sum(new_sum_elements)
                        if current_sum < min_sum:
                            min_sum = current_sum
                            solution = (i, j, number)
                    grid[i][j] = 'x'
    return solution

def is_valid(grid, row, col, number):
    for i in range(3):
        if grid[i][col] != 'x' and grid[i][col] == number:
            return False
        if grid[row][i] != 'x' and grid[row][i] == number:
            return False
    if row > 0 and grid[row-1][col] != 'x' and grid[row-1][col] >= number:
        return False
    if col > 0 and grid[row][col-1] != 'x' and grid[row][col-1] >= number:
        return False
    if row < 2 and grid[row+1][col] != 'x' and grid[row+1][col] <= number:
        return False
    if col < 2 and grid[row][col+1] != 'x' and grid[row][col+1] <= number:
        return False
    return True

grid = np.array([['x', 'x', 42], ['x', 46, 'x'], ['x', 'x', 55]])
numbers = list(range(25, 58))
numbers.remove(42)
numbers.remove(46)
numbers.remove(55)
solution = solve(grid, numbers, [42, 46, 55])
print(solution)
