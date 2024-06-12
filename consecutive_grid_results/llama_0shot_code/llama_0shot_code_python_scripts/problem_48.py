
def solve_grid(grid):
    # List of numbers from 40 to 80
    numbers = list(range(40, 80))

    replacements = []

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 'x':
                replacements.append((i, j, numbers.pop(0))) # pop the first number from the list
                grid[i][j] = replacements[-1][2] # update the grid with the new number

    # Calculate the sum of the numbers in the topmost row, rightmost column and diagonal
    top_row_sum = sum(grid[0])
    right_col_sum = sum(grid[i][-1] for i in range(len(grid)))
    diagonal_sum = sum(grid[i][i] for i in range(len(grid)))
    total_sum = top_row_sum + right_col_sum + diagonal_sum

    return replacements, total_sum

# Initial state of the grid
grid = [['x', '53', 'x', '79'],
        ['46', '51', 'x', '78'],
        ['45', 'x', '73', '77'],
        ['42', '47', 'x', 'x']]

replacements, total_sum = solve_grid(grid)

print("Replacements:", replacements)
print("Minimized sum:", total_sum)
