
import numpy as np

def is_valid(grid, row, col, num):
    # Check if the number already exists in the same row or column
    for x in range(9):
        if grid[row][x] == num or grid[x][col] == num:
            return False

    # Check if the number already exists in the same 3x3 sub-grid
    start_row = row - row % 3
    start_col = col - col % 3
    for i in range(3):
        for j in range(3):
            if grid[i + start_row][j + start_col] == num:
                return False

    return True

def solve_magic_square(grid, row=0, col=0):
    # If we have reached the 8th row and 9th column (0 indexed matrix),
    # we are returning true to signal that we have found a solution
    if (row == 3 - 1 and col == 3):
        return True

    # If column value becomes 3, we move to next row
    # and column start from 0
    if col == 3:
        row += 1
        col = 0

    # If the current position of the grid already contains value > 0, we iterate for next column
    if grid[row][col] > 0:
        return solve_magic_square(grid, row, col + 1)

    for num in range(40, 90):
        # Check if it is safe to place the num (1-9) in the given row, col
        # If yes then place the number in the current (row, col) position of the grid
        # and check whether this placement leads to a solution or not
        if is_valid(grid, row, col, num):
            grid[row][col] = num
            if solve_magic_square(grid, row, col + 1):
                return True

        # If placing the current number in the current (row, col) position of the grid
        # does not lead to a solution, then remove this number (backtrack) and try next number
        grid[row][col] = 0

    return False

grid = [[0, 0, 0], [80, 48, 0], [0, 0, 0]]

if (solve_magic_square(grid)):
    print(grid)
else:
    print("No solution exists")
