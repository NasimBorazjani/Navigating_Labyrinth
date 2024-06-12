
def solve_grid(grid):
    # Create a list of all possible numbers in the given range
    possible_numbers = list(range(22, 72))

    # List to store the replacements
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

    # Calculate the sum of the numbers in the topmost row, the numbers in the rightmost column, and the numbers in the diagonal
    top_row_sum = sum(grid[0])
    right_column_sum = sum(grid[i][-1] for i in range(len(grid)))
    diagonal_sum = sum(grid[i][i] for i in range(len(grid)))
    total_sum = top_row_sum + right_column_sum + diagonal_sum

    # Return the list of replacements and the total sum
    return replacements, total_sum

# Test the function
grid = [['37', '50', 'x', '70'],
        ['x', '46', 'x', '65'],
        ['41', '43', 'x', '49'],
        ['x', '30', 'x', 'x']]

replacements, total_sum = solve_grid(grid)
print("Replacements:", replacements)
print("Total Sum:", total_sum)
