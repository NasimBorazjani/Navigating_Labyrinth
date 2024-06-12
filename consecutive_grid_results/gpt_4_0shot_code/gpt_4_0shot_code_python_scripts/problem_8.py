
import numpy as np

def solve(grid, numbers, sum_elements):
    # Find the next cell to fill
    for i in range(3):
        for j in range(3):
            if grid[i][j] == 'x':
                # Try to fill the cell with each number in the range
                for number in numbers:
                    # Check if the number can be placed in the cell
                    if is_valid(grid, i, j, number):
                        # Place the number in the cell
                        grid[i][j] = number
                        # Remove the number from the available numbers
                        numbers.remove(number)
                        # Update the sum of the elements
                        if i == 0 or j == 2 or i == j:
                            sum_elements += number
                        # Recursively try to fill the rest of the grid
                        if solve(grid, numbers, sum_elements):
                            return True
                        # If the number leads to a conflict, backtrack
                        else:
                            grid[i][j] = 'x'
                            numbers.append(number)
                            if i == 0 or j == 2 or i == j:
                                sum_elements -= number
                # If no number can be placed in the cell, return False
                return False
    # If all cells are filled, return True
    return True

def is_valid(grid, row, col, number):
    # Check the row
    for j in range(3):
        if grid[row][j] == number:
            return False
    # Check the column
    for i in range(3):
        if grid[i][col] == number:
            return False
    # Check the increasing or decreasing order
    if row > 0 and grid[row-1][col] != 'x' and grid[row-1][col] < number:
        return False
    if col > 0 and grid[row][col-1] != 'x' and grid[row][col-1] < number:
        return False
    return True

# Initialize the grid and the available numbers
grid = [['x', 'x', 'x'], ['x', '36', '44'], ['x', '34', 'x']]
numbers = [str(i) for i in range(19, 53) if str(i) not in np.array(grid).flatten()]
sum_elements = 0

# Solve the grid
solve(grid, numbers, sum_elements)

# Print the solution
for i in range(3):
    for j in range(3):
        if grid[i][j] != 'x':
            print((i, j, grid[i][j]))
