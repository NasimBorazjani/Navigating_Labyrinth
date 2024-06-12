
def solve_grid(grid):
    # List of all possible numbers in the given range
    possible_numbers = list(range(22, 67))

    replacements = []

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 'x':
                # Replace 'x' with the smallest possible number
                grid[i][j] = possible_numbers.pop(0)
                replacements.append((i, j, grid[i][j]))

    # Calculate the sum of the numbers in the topmost row, rightmost column and diagonal
    top_row_sum = sum(grid[0])
    right_col_sum = sum(grid[i][-1] for i in range(len(grid)))
    diagonal_sum = sum(grid[i][i] for i in range(len(grid)))

    total_sum = top_row_sum + right_col_sum + diagonal_sum

    return replacements, total_sum

# Initial state of the grid
grid = [['22', 'x', 'x', '66'],
        ['x', 'x', 'x', 'x'],
        ['50', '52', 'x', '57'],
        ['x', '55', 'x', 'x']]

replacements, total_sum = solve_grid(grid)

print("Replacements:", replacements)
print("Minimized sum:", total_sum)
