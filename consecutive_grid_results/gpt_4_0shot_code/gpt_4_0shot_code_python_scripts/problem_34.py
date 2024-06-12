
import numpy as np

# Initialize the grid
grid = np.array([[38, 'x', 77], ['x', 'x', 'x'], ['x', 52, 'x']])

# Initialize the list of available numbers
available_numbers = list(range(38, 87))
available_numbers.remove(38)
available_numbers.remove(77)
available_numbers.remove(52)

# Initialize the list of replacements
replacements = []

# Function to check if a number can be placed at a certain position in the grid
def can_place(grid, row, col, num):
    # Check the row
    for i in range(3):
        if grid[row][i] != 'x' and grid[row][i] == num:
            return False
    # Check the column
    for i in range(3):
        if grid[i][col] != 'x' and grid[i][col] == num:
            return False
    return True

# Function to solve the grid
def solve(grid):
    # Find the next empty position
    for i in range(3):
        for j in range(3):
            if grid[i][j] == 'x':
                # Try to place a number at the empty position
                for num in available_numbers:
                    if can_place(grid, i, j, num):
                        grid[i][j] = num
                        available_numbers.remove(num)
                        replacements.append((i, j, num))
                        if solve(grid):
                            return True
                        # Undo the current move and try the next number
                        grid[i][j] = 'x'
                        available_numbers.append(num)
                        replacements.remove((i, j, num))
                return False
    return True

# Solve the grid
solve(grid)

# Print the replacements
print(replacements)
