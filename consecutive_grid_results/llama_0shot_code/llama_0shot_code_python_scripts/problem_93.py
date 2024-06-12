
def solve_grid(grid):
    # Create a list of all possible numbers within the given range
    possible_numbers = list(range(36, 91))

    # List to store the replacements made in the grid
    replacements = []

    # Iterate over each cell in the grid
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            # If the cell contains an 'x'
            if grid[i][j] == 'x':
                # Replace it with the smallest possible number and remove this number from the list
                replaced_number = possible_numbers.pop(0)
                grid[i][j] = replaced_number
                replacements.append((i, j, replaced_number))

    # Calculate the sum of the numbers in the topmost row, the rightmost column, and the diagonal
    top_row_sum = sum(grid[0])
    right_col_sum = sum(grid[i][-1] for i in range(len(grid)))
    diagonal_sum = sum(grid[i][i] for i in range(len(grid)))
    total_sum = top_row_sum + right_col_sum + diagonal_sum

    # Return the list of tuples representing the replacements made in the grid and the total sum
    return replacements, total_sum

# Test the function with the given grid
grid = [['38', 'x', '50', 'x'], ['x', 'x', '64', '67'], ['54', 'x', '71', '79'], ['x', '59', '89', '90']]
replacements, total_sum = solve_grid(grid)
print("Replacements:", replacements)
print("Total Sum:", total_sum)
