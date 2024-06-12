
# Initial grid
grid = [['38', 'x', '77'],
        ['x', 'x', 'x'],
        ['x', '52', 'x']]

# Function to check if a number can be placed in a certain position in the grid
def is_valid(grid, row, col, num):
    # Check the number in the row
    for i in range(3):
        if grid[row][i] != 'x' and int(grid[row][i]) > num:
            return False
    # Check the number in the column
    for i in range(3):
        if grid[i][col] != 'x' and int(grid[i][col]) > num:
            return False
    # Check the number in the diagonal
    if row == col and grid[0][0] != 'x' and int(grid[0][0]) > num:
        return False
    return True

# List of possible numbers
possible_numbers = list(range(39, 86))

# Remove the numbers that don't meet the conditions
for i in range(3):
    for j in range(3):
        if grid[i][j] == 'x':
            possible_numbers = [num for num in possible_numbers if is_valid(grid, i, j, num)]

# Sort the possible numbers in ascending order
possible_numbers.sort()

# Fill the grid with the possible numbers
for i in range(3):
    for j in range(3):
        if grid[i][j] == 'x':
            grid[i][j] = str(possible_numbers.pop(0))

# Print the resulting grid and the replacements as a list of tuples
print(grid)
replacements = [(i, j, int(grid[i][j])) for i in range(3) for j in range(3) if grid[i][j] != 'x']
print(replacements)
