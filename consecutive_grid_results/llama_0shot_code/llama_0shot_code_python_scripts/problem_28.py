
from itertools import permutations

# Initial grid
grid = [['12', 'x', 'x'], ['18', 'x', '52'], ['22', 'x', '31']]

# Possible numbers that can fill the grid
possible_numbers = list(range(13, 60))

# Function to check if a number can be placed at a certain position in the grid
def is_valid(grid, row, col, num):
    # Check the number in the row
    if col > 0 and int(grid[row][col-1]) >= num:
        return False
    if col < 2 and int(grid[row][col+1]) <= num:
        return False

    # Check the number in the column
    if row > 0 and int(grid[row-1][col]) >= num:
        return False
    if row < 2 and int(grid[row+1][col]) <= num:
        return False

    return True

# Remove invalid numbers from the possible numbers list
for i in range(3):
    for j in range(3):
        if grid[i][j] == 'x':
            grid[i][j] = 0
        else:
            grid[i][j] = int(grid[i][j])
        possible_numbers = [num for num in possible_numbers if is_valid(grid, i, j, num)]

# Minimize the sum by filling the grid with the smallest possible numbers first
possible_numbers.sort()

# Fill the grid with the remaining possible numbers
for i in range(3):
    for j in range(3):
        if grid[i][j] == 0:
            for num in possible_numbers:
                if is_valid(grid, i, j, num):
                    grid[i][j] = num
                    break

# Print the resulting grid and the replacements as a list of tuples
print("Grid:")
for row in grid:
    print(row)

replacements = [(i, j, grid[i][j]) for i in range(3) for j in range(3) if grid_init[i][j] == 'x']
print("Replacements:", replacements)
