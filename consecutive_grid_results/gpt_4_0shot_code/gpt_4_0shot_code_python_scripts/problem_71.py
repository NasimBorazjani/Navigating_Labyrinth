
import numpy as np

# Define the initial grid
grid = np.array([['x', 53, 60, 67],
                 ['x', 'x', 72, 'x'],
                 [50, 56, 74, 'x'],
                 [54, 65, 76, 'x']])

# Define the range of possible numbers
numbers = set(range(28, 79))

# Remove the numbers already in the grid from the set of possible numbers
for row in grid:
    for num in row:
        if num != 'x':
            numbers.remove(num)

# Define a function to check if a list of numbers is strictly increasing or decreasing
def check_strictly_increasing_or_decreasing(lst):
    return all(x<y for x, y in zip(lst, lst[1:])) or all(x>y for x, y in zip(lst, lst[1:]))

# Define a function to replace 'x' in the grid
def replace_x(grid, numbers):
    replacements = []
    for i in range(4):
        for j in range(4):
            if grid[i][j] == 'x':
                for num in numbers:
                    temp_grid = grid.copy()
                    temp_grid[i][j] = num
                    if check_strictly_increasing_or_decreasing(temp_grid[i,:]) and check_strictly_increasing_or_decreasing(temp_grid[:,j]):
                        grid[i][j] = num
                        numbers.remove(num)
                        replacements.append((i, j, num))
                        break
    return replacements

# Call the function to replace 'x' in the grid
replacements = replace_x(grid, numbers)

# Print the replacements
print(replacements)
