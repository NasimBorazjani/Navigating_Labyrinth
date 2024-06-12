
def solve_grid(grid):
    # List of numbers from 10 to 50
    numbers = list(range(10, 50))

    # List to store the replacements
    replacements = []

    # Replace 'x's with the smallest possible number
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 'x':
                grid[i][j] = numbers.pop(0)
                replacements.append((i, j, grid[i][j]))

    # Calculate the sum of the numbers in the topmost row, rightmost column, and the diagonal
    top_row_sum = sum(grid[0])
    right_col_sum = sum(grid[i][-1] for i in range(len(grid)))
    diagonal_sum = sum(grid[i][i] for i in range(len(grid)))
    total_sum = top_row_sum + right_col_sum + diagonal_sum

    # Return the list of replacements and the total sum
    return replacements, total_sum

# Test the function
grid = [['x', '38', '19', 'x'], ['22', 'x', 'x', 'x'], ['x', '30', 'x', '42'], ['x', 'x', '35', '45']]
replacements, total_sum = solve_grid(grid)
print("Replacements:", replacements)
print("Total Sum:", total_sum)
