
def can_place(grid, row, col, num):
    # Check the number is not in the current row, column or diagonal
    for i in range(4):
        if grid[row][i] == num or grid[i][col] == num:
            return False
    if row == col:
        for i in range(4):
            if grid[i][i] == num:
                return False
    if row + col == 3:
        for i in range(4):
            if grid[i][3 - i] == num:
                return False
    return True

def solve(grid, row=0, col=0):
    if row == 4:
        return True
    if col == 4:
        return solve(grid, row + 1, 0)
    if grid[row][col] != 'x':
        return solve(grid, row, col + 1)
    for num in range(28, 60):
        if can_place(grid, row, col, num):
            grid[row][col] = num
            if solve(grid, row, col + 1):
                return True
            grid[row][col] = 'x'
    return False

def magic_square():
    grid = [['30', 'x', 'x', '37'],
            ['41', '56', 'x', 'x'],
            ['x', 'x', '29', '55'],
            ['x', 'x', 'x', '42']]
    solve(grid)
    return [(row, col, num) for row in range(4) for col in range(4) for num in range(28, 60) if grid[row][col] == num]

print(magic_square())
