
def solve_grid(grid):
    # Create a list of all possible numbers in the given range
    possible_numbers = list(range(28, 83))

    # List to store the replacements made
    replacements = []

    # Go through each cell in the grid
    for i in range(4):
        for j in range(4):
            # If the cell contains an 'x'
            if grid[i][j] == 'x':
                # Replace it with the smallest possible number and remove this number from the list
                replaced_number = possible_numbers.pop(0)
                grid[i][j] = replaced_number
                replacements.append((i, j, replaced_number))

    # Calculate the sum of the numbers in the topmost row, rightmost column, and the diagonal
    top_row_sum = sum(grid[0])
    right_column_sum = sum(grid[i][3] for i in range(4))
    diagonal_sum = grid[0][0] + grid[1][1] + grid[2][2] + grid[3][3]

    # Return the list of replacements and the minimum sum
    return replacements, top_row_sum + right_column_sum + diagonal_sum

# Test the function with the given grid
grid = [['81', '52', 'x', 'x'], ['x', '50', '53', 'x'], ['42', 'x', '54', '74'], ['x', 'x', '56', '77']]
print(solve_grid(grid))
