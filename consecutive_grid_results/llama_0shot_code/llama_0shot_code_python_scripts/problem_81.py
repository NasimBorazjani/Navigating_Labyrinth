
def solve_grid(grid):
    # Create a list of all possible numbers in the given range
    possible_numbers = list(range(37, 87))

    # List to store the replacements made in the grid
    replacements = []

    # Iterate over each cell in the grid
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            # If the cell contains an 'x'
            if grid[i][j] == 'x':
                # Replace it with the smallest possible number from the list
                grid[i][j] = possible_numbers.pop(0)
                # Add the replacement to the list of replacements
                replacements.append((i, j, grid[i][j]))

    # Calculate the sum of the numbers in the topmost row, rightmost column, and the diagonal
    top_row_sum = sum(grid[0])
    right_col_sum = sum(grid[i][-1] for i in range(len(grid)))
    diagonal_sum = sum(grid[i][i] for i in range(len(grid)))
    total_sum = top_row_sum + right_col_sum + diagonal_sum

    # Return the list of replacements and the total sum
    return replacements, total_sum

# Test the function with the given grid
grid = [['47', '51', 'x', '64'],
        ['50', '53', 'x', 'x'],
        ['x', '55', '68', '74'],
        ['x', 'x', '72', 'x']]

replacements, total_sum = solve_grid(grid)
print("Replacements:", replacements)
print("Total Sum:", total_sum)
