
def find_next_cell(grid, row, col):
    while row < len(grid) and col < len(grid[0]):
        if grid[row][col] is None:
            return row, col
        row += 1
        col += 1
    return -1, -1

def is_valid(grid, row, col, num):
    # Check the number in the row
    for r in range(row, len(grid)):
        if grid[r][col] is not None and grid[r][col] <= num:
            return False
    # Check the number in the column
    for c in range(col, len(grid[0])):
        if grid[row][c] is not None and grid[row][c] <= num:
            return False
    # Check the number in the diagonal
    while row < len(grid) and col < len(grid[0]):
        if grid[row][col] is not None and grid[row][col] <= num:
            return False
        row += 1
        col += 1
    return True

def solve_grid(grid):
    replacements = []
    row, col = 0, 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 'x':
                grid[r][c] = None
    num = 7
    while num < 60:
        if grid[row][col] is None:
            if is_valid(grid, row, col, num):
                grid[row][col] = num
                replacements.append((row, col, num))
                row, col = find_next_cell(grid, row, col)
                num += 1
            else:
                num += 1
        else:
            row, col = find_next_cell(grid, row, col)
    return replacements

grid = [['13', 'x', 'x'], ['x', 'x', '27'], ['x', '26', 'x']]
print(solve_grid(grid))
