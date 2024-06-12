
def solve_grid(grid):
    # List of all possible numbers within the given range
    numbers = list(range(18, 68))

    # List to store the replacements
    replacements = []

    # Iterate over each cell in the grid
    for i in range(4):
        for j in range(4):
            # If the cell contains 'x'
            if grid[i][j] == 'x':
                # Replace 'x' with the smallest possible number and remove this number from the list
                replaced_number = numbers.pop(0)
                grid[i][j] = replaced_number
                replacements.append((i, j, replaced_number))

    # Calculate the sum of the topmost row, the rightmost column, and the diagonal
    top_row_sum = sum(grid[0])
    right_col_sum = sum(grid[i][3] for i in range(4))
    diagonal_sum = grid[0][0] + grid[1][1] + grid[2][2] + grid[3][3]

    # Return the list of replacements and the minimum sum
    return replacements, top_row_sum + right_col_sum + diagonal_sum

# Initial state of the grid
grid = [['20', 'x', '34', 'x'],
        ['x', 'x', '43', 'x'],
        ['x', 'x', '48', 'x'],
        ['65', 'x', 'x', '48']]

replacements, min_sum = solve_grid(grid)
print("Replacements:", replacements)
print("Minimum Sum:", min_sum)
