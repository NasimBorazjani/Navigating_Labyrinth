
import itertools

# Possible range of numbers
possible_numbers = list(range(35, 80))

# Initial grid with 'x' values
grid = [['x', '73', '74', 'x'],
        ['46', 'x', '63', '72'],
        ['x', '47', 'x', 'x'],
        ['41', '45', 'x', '54']]

# Function to check if a number can be placed at a position in the grid
def is_valid(grid, num, pos):
    # Check the number in the row
    for i in range(len(grid)):
        if grid[i][pos] != 'x' and int(grid[i][pos]) > num:
            return False
    # Check the number in the column
    for i in range(len(grid)):
        if grid[pos][i] != 'x' and int(grid[pos][i]) > num:
            return False
    # Check the number in the diagonal
    if pos == len(grid) - 1:
        for i in range(len(grid)):
            if grid[i][i] != 'x' and int(grid[i][i]) > num:
                return False
    return True

# Function to find the 'x' positions and replace them with valid numbers
def replace_x(grid, possible_numbers):
    x_positions = []
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 'x':
                x_positions.append((i, j))
    combinations = itertools.permutations(possible_numbers, len(x_positions))
    min_sum = float('inf')
    for combination in combinations:
        temp_grid = [row.copy() for row in grid]
        for (x_pos, num) in zip(x_positions, combination):
            if is_valid(temp_grid, num, x_pos[1]):
                temp_grid[x_pos[0]][x_pos[1]] = num
        sum_temp_grid = sum(int(temp_grid[0][i]) for i in range(len(temp_grid[0]))) + \
                         sum(int(temp_grid[i][-1]) for i in range(len(temp_grid))) + \
                         sum(temp_grid[i][i] for i in range(len(temp_grid)))
        if sum_temp_grid < min_sum:
            min_sum = sum_temp_grid
            min_grid = temp_grid
    return min_grid

# Call the function to replace the 'x' values and get the minimum sum grid
min_grid = replace_x(grid, possible_numbers)

# Print the replaced 'x' values and their positions
replacements = []
for i in range(len(min_grid)):
    for j in range(len(min_grid[i])):
        if min_grid[i][j] != 'x':
            replacements.append((i, j, min_grid[i][j]))
print(replacements)
