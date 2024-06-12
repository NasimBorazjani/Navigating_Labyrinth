
def solve_grid():
    grid = [['10', '15', '39'], ['x', '27', '29'], ['x', 'x', 'x']]
    remaining_numbers = list(range(8, 41))
    replacements = []

    # Fill in the missing values
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 'x':
                grid[i][j] = str(remaining_numbers.pop(0))
                replacements.append((i, j, int(grid[i][j])))

    # Check if the numbers are in strictly increasing or decreasing order
    for i in range(len(grid)):
        if grid[i] != sorted(grid[i], key=int) and grid[i] != sorted(grid[i], key=int, reverse=True):
            return "No solution"

    for j in range(len(grid[0])):
        column = [grid[i][j] for i in range(len(grid))]
        if column != sorted(column, key=int) and column != sorted(column, key=int, reverse=True):
            return "No solution"

    # Calculate the sum of the numbers in the top row, rightmost column, and diagonal
    top_row_sum = sum(map(int, grid[0]))
    rightmost_column_sum = sum(map(int, [grid[i][-1] for i in range(len(grid))]))
    diagonal_sum = sum(map(int, [grid[i][i] for i in range(len(grid))]))
    total_sum = top_row_sum + rightmost_column_sum + diagonal_sum

    return replacements, total_sum

print(solve_grid())
