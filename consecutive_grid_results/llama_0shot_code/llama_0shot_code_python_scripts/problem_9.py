
def solve_grid():
    # Possible numbers in the grid
    numbers = list(range(34, 67))

    # Initial grid
    grid = [['x', 'x', 'x'], ['x', '51', 'x'], ['x', '61', '64']]

    # Replacements
    replacements = []

    # Fill the grid
    for i in range(3):
        for j in range(3):
            if grid[i][j] == 'x':
                if i == 0 or i == 1 and grid[i-1][j] > grid[i][j+1] or i == 2 and grid[i-1][j] < grid[i][j+1]:
                    grid[i][j] = numbers.pop(0)
                else:
                    grid[i][j] = numbers.pop()
                replacements.append((i, j, grid[i][j]))

    # Calculate the sum
    sum_top_row = sum(grid[0])
    sum_right_col = sum([grid[i][2] for i in range(3)])
    sum_diag = grid[0][0] + grid[1][1] + grid[2][2]
    total_sum = sum_top_row + sum_right_col + sum_diag

    # Return the replacements and the total sum
    return replacements, total_sum

replacements, total_sum = solve_grid()
print(replacements)
print(total_sum)
