
import numpy as np

# Initialize the grid
grid = np.array([['x', 'x', 85],
                 [58, 'x', 84],
                 ['x', 74, 59]])

# Initialize the list of available numbers
available_numbers = list(range(48, 92))
for row in grid:
    for cell in row:
        if cell != 'x':
            available_numbers.remove(cell)

# Initialize the list of replacements
replacements = []

def solve(grid, available_numbers, replacements):
    # Find the first 'x' in the grid
    for i in range(3):
        for j in range(3):
            if grid[i, j] == 'x':
                # Try to replace the 'x' with each available number
                for number in available_numbers:
                    grid[i, j] = number
                    available_numbers.remove(number)
                    replacements.append((i, j, number))
                    
                    # Check if the grid is valid
                    if is_valid(grid):
                        # If the grid is valid, try to solve the rest of the grid
                        if solve(grid, available_numbers, replacements):
                            return True
                    
                    # If the grid is not valid or the rest of the grid cannot be solved,
                    # undo the replacement and try the next number
                    grid[i, j] = 'x'
                    available_numbers.append(number)
                    replacements.remove((i, j, number))
                
                # If no number can be placed in the current cell, return False
                return False
    
    # If there are no 'x's in the grid, return True
    return True

def is_valid(grid):
    # Check the rows
    for row in grid:
        if not is_increasing_or_decreasing(row):
            return False
    
    # Check the columns
    for column in grid.T:
        if not is_increasing_or_decreasing(column):
            return False
    
    # Check the diagonal
    diagonal = np.array([grid[i, i] for i in range(3)])
    if not is_increasing_or_decreasing(diagonal):
        return False
    
    return True

def is_increasing_or_decreasing(array):
    return all(array[i] <= array[i + 1] for i in range(len(array) - 1)) or \
           all(array[i] >= array[i + 1] for i in range(len(array) - 1))

# Solve the grid
solve(grid, available_numbers, replacements)

# Print the replacements
print(replacements)
