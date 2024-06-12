
import numpy as np

# Define the initial grid
grid = np.array([['x', 58, 'x'], [42, 'x', 70], ['x', 'x', 'x']])

# Define the range of possible numbers
numbers = list(range(31, 85))

# Remove the numbers already in the grid from the list of possible numbers
for row in grid:
    for num in row:
        if num != 'x' and num in numbers:
            numbers.remove(num)

# Define the function to check if a row or column is strictly increasing or decreasing
def is_strictly_increasing_or_decreasing(lst):
    return all(x<y for x, y in zip(lst, lst[1:])) or all(x>y for x, y in zip(lst, lst[1:]))

# Define the function to replace 'x' in the grid
def replace_x(grid, numbers):
    replacements = []
    for i in range(3):
        for j in range(3):
            if grid[i][j] == 'x':
                for num in numbers:
                    grid[i][j] = num
                    if is_strictly_increasing_or_decreasing(grid[i]) and is_strictly_increasing_or_decreasing(grid[:,j]):
                        replacements.append((i, j, num))
                        numbers.remove(num)
                        break
                    else:
                        grid[i][j] = 'x'
    return replacements

# Call the function to replace 'x' in the grid
replacements = replace_x(grid, numbers)

# Print the replacements
print(replacements)
