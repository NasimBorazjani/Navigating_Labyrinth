
import numpy as np

# Initialize the grid
grid = np.array([['10', '15', '39'], ['x', '27', '29'], ['x', 'x', 'x']])

# Initialize the list of available numbers
available_numbers = list(map(str, range(8, 42)))
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
                    replacements.append((i, j, int(number)))
                    
                    # Check if the grid is valid
                    if is_valid(grid):
                        # If the grid is valid, try to solve the rest of the grid
                        if solve(grid, available_numbers, replacements):
                            return True
                    
                    # If the grid is not valid or the rest of the grid cannot be solved, undo the replacement
                    grid[i, j] = 'x'
                    available_numbers.append(number)
                    replacements.remove((i, j, int(number)))
                
                # If no available number can be used to replace the 'x', return False
                return False
    
    # If there is no 'x' in the grid, return True
    return True

def is_valid(grid):
    # Check if the numbers in each row and column are strictly increasing or decreasing
    for i in range(3):
        if not (np.all(np.diff(grid[i, :].astype(int)) > 0) or np.all(np.diff(grid[i, :].astype(int)) < 0)):
            return False
        if not (np.all(np.diff(grid[:, i].astype(int)) > 0) or np.all(np.diff(grid[:, i].astype(int)) < 0)):
            return False
    
    # Check if the numbers in the diagonal are strictly increasing or decreasing
    if not (np.all(np.diff(grid.diagonal().astype(int)) > 0) or np.all(np.diff(grid.diagonal().astype(int)) < 0)):
        return False
    
    return True

# Solve the grid
solve(grid, available_numbers, replacements)

# Print the replacements
print(replacements)
