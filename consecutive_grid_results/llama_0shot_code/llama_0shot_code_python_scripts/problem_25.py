
def solve_grid():
    # The given range of numbers
    range_start = 29
    range_end = 72

    # Initialize the grid
    grid = [['x', 'x', 'x'], ['39', 'x', '52'], ['60', 'x', 'x']]

    # Fill in the missing values in the grid
    for i in range(3):
        for j in range(3):
            if grid[i][j] == 'x':
                for num in range(range_start, range_end):
                    if num not in [int(val) for val in grid[i]] and num not in [int(val) for val in grid[j]]:
                        grid[i][j] = num
                        break

    # Check if the numbers in each row and column are in strictly increasing or decreasing order
    for i in range(3):
        row = [int(val) for val in grid[i]]
        col = [int(val) for val in grid[i][::-1]]
        if row != sorted(row) and row != sorted(row, reverse=True):
            return "No solution"
        if col != sorted(col) and col != sorted(col, reverse=True):
            return "No solution"

    # Calculate the sum of the numbers in the topmost row, the numbers in the rightmost column, and the numbers on the diagonal
    top_row_sum = sum([int(val) for val in grid[0]])
    right_col_sum = sum([int(val) for val in grid[::-1]])
    diagonal_sum = int(grid[0][0]) + int(grid[1][1]) + int(grid[2][2])
    total_sum = top_row_sum + right_col_sum + diagonal_sum

    # Prepare the replacements
    replacements = [(i, j, int(grid[i][j])) for i in range(3) for j in range(3) if grid[i][j] != 'x']

    return replacements, total_sum

print(solve_grid())
