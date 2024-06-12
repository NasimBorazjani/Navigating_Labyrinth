
import numpy as np

# Initialize the grid
grid = np.array([['x', 'x', 'x'], [39, 'x', 50], [32, 'x', 55]])

# Initialize the list of available numbers
available_numbers = list(range(29, 83))
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
                    # Check if the number can be placed in the current position
                    if check_placement(grid, i, j, number):
                        # Replace the 'x' with the number
                        grid[i, j] = number
                        available_numbers.remove(number)
                        replacements.append((i, j, number))
                        # Recursively try to solve the rest of the grid
                        if solve(grid, available_numbers, replacements):
                            return True
                        # If the number leads to a conflict, undo the replacement
                        grid[i, j] = 'x'
                        available_numbers.append(number)
                        replacements.remove((i, j, number))
                # If no number can be placed in the current position, backtrack
                return False
    # If the grid is completely filled, the problem is solved
    return True

def check_placement(grid, row, col, number):
    # Check the row
    row_numbers = [cell for cell in grid[row, :] if cell != 'x']
    if row_numbers and (number <= min(row_numbers) or number >= max(row_numbers)):
        return False
    # Check the column
    col_numbers = [cell for cell in grid[:, col] if cell != 'x']
    if col_numbers and (number <= min(col_numbers) or number >= max(col_numbers)):
        return False
    # Check the diagonal
    if row == col:
        diag_numbers = [grid[i, i] for i in range(3) if grid[i, i] != 'x']
        if diag_numbers and (number <= min(diag_numbers) or number >= max(diag_numbers)):
            return False
    return True

# Solve the problem
solve(grid, available_numbers, replacements)
print(replacements)
