
def solve_grid(grid):
    # List of all possible numbers between 10 and 65 (inclusive)
    possible_numbers = list(range(10, 65))

    replacements = []

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 'x':
                # Replace 'x' with the smallest possible number and remove this number from the list
                grid[i][j] = possible_numbers.pop(0)
                replacements.append((i, j, grid[i][j]))

    # Calculate the sum of the numbers in the topmost row, rightmost column, and the diagonal
    top_row_sum = sum(grid[0])
    right_col_sum = sum(grid[i][-1] for i in range(len(grid)))
    diagonal_sum = sum(grid[i][i] for i in range(len(grid)))

    total_sum = top_row_sum + right_col_sum + diagonal_sum

    return replacements, total_sum


# Initial state of the grid
grid = [['x', '21', 'x', 'x'],
        ['18', '27', 'x', '51'],
        ['24', '29', 'x', 'x'],
        ['54', '33', '25', '12']]

replacements, total_sum = solve_grid(grid)

print("Replacements:", replacements)
print("Minimized sum:", total_sum)
