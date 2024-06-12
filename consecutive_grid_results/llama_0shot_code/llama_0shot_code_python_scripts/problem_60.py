
def is_valid(grid, row, col, num):
    # Check the number in the row
    for x in range(4):
        if grid[row][x] == num:
            return False

    # Check the number in the column
    for x in range(4):
        if grid[x][col] == num:
            return False

    # Check the number in the diagonal
    if row == col:
        for x in range(4):
            if grid[x][x] == num:
                return False

    return True


def find_empty(grid):
    for i in range(4):
        for j in range(4):
            if grid[i][j] == 'x':
                return i, j  # row, col

    return None


def solve_sudoku(grid):
    find = find_empty(grid)
    if not find:
        return grid
    else:
        row, col = find

    for i in range(24, 64):
        if is_valid(grid, row, col, i):
            grid[row][col] = i

            if solve_sudoku(grid):
                return [(row, col, i)] + solve_sudoku(grid)

            grid[row][col] = 'x'

    return []


grid = [['x', 'x', 'x', 'x'],
        ['37', 'x', '49', 'x'],
        ['x', '44', 'x', 'x'],
        ['42', 'x', '51', '61']]

solution = solve_sudoku(grid)
print(solution)
