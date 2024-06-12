
import numpy as np

# Initialize the grid
grid = np.array([[46, 80, 90], [51, 'x', 'x'], ['x', 'x', 'x']])

# Initialize the list of available numbers
available_numbers = list(range(45, 99))
for row in grid:
    for num in row:
        if num != 'x':
            available_numbers.remove(num)

# Initialize the list of replacements
replacements = []

def solve(grid, available_numbers, replacements):
    # Find the first 'x' in the grid
    for i in range(3):
        for j in range(3):
            if grid[i, j] == 'x':
                # Try to replace the 'x' with each available number
                for num in available_numbers:
                    grid[i, j] = num
                    available_numbers.remove(num)
                    replacements.append((i, j, num))
                    
                    # Check if the grid is valid
                    if is_valid(grid):
                        # If the grid is valid, try to solve the rest of the grid
                        if solve(grid, available_numbers, replacements):
                            return True
                    
                    # If the grid is not valid or the rest of the grid cannot be solved, undo the replacement
                    grid[i, j] = 'x'
                    available_numbers.append(num)
                    replacements.remove((i, j, num))
                
                # If no available number can be used to replace the 'x', return False
                return False
    
    # If there is no 'x' in the grid, return True
    return True

def is_valid(grid):
    # Check the rows
    for row in grid:
        if not is_increasing_or_decreasing(row):
            return False
    
    # Check the columns
    for col in grid.T:
        if not is_increasing_or_decreasing(col):
            return False
    
    # Check the diagonal
    if not is_increasing_or_decreasing(np.diag(grid)):
        return False
    
    return True

def is_increasing_or_decreasing(arr):
    return np.all(np.diff(arr) > 0) or np.all(np.diff(arr) < 0)

# Solve the grid
solve(grid, available_numbers, replacements)

# Print the replacements
print(replacements)
