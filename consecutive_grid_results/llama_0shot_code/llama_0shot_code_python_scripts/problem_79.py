
def solve_grid(grid):
    # List of all possible numbers between 14 and 64 (inclusive)
    possible_numbers = list(range(14, 64))

    # List to store the replacements made in the grid
    replacements = []

    # Iterate over each cell in the grid
    for i in range(4):
        for j in range(4):
            # If the cell is marked with an 'x'
            if grid[i][j] == 'x':
                # Replace it with the smallest possible number and remove this number from the list
                grid[i][j] = possible_numbers.pop(0)
                replacements.append((i, j, grid[i][j]))

    # Calculate the sum of the numbers in the topmost row, the rightmost column, and the diagonal
    top_row_sum = sum(grid[0])
    right_col_sum = sum(grid[i][3] for i in range(4))
    diagonal_sum = grid[0][0] + grid[1][1] + grid[2][2] + grid[3][3]

    # Return the list of replacements and the minimum sum
    return replacements, top_row_sum + right_col_sum + diagonal_sum

# Initial state of the grid
grid = [['x', 'x', '53', '62'],
        ['x', '27', 'x', 'x'],
        ['21', '22', 'x', '50'],
        ['x', '20', '25', '44']]

replacements, min_sum = solve_grid(grid)
print("Replacements:", replacements)
print("Minimum Sum:", min_sum)
