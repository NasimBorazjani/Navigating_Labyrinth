
def is_valid(grid, row, col, num):
    # Check the number in the row
    if num in grid[row]:
        return False
    # Check the number in the column
    if num in zip(*grid)[col]:
        return False
    # Check the number in the diagonal
    if row == col and num in [grid[i][i] for i in range(4)]:
        return False
    if row + col == 3 and num in [grid[i][3 - i] for i in range(4)]:
        return False
    return True

def solve(grid, row=0, col=0):
    if row == 4:
        return grid
    if col == 4:
        return solve(grid, row + 1, 0)
    if grid[row][col] != 'x':
        return solve(grid, row, col + 1)
    for num in range(30, 87):
        if is_valid(grid, row, col, num):
            grid[row][col] = num
            solution = solve(grid, row, col + 1)
            if solution:
                return solution
            grid[row][col] = 'x'
    return None

def magic_square(grid):
    solution = solve(grid)
    result = [(i, j, val) for i in range(4) for j in range(4) if (i, j, val := solution[i][j]) != 'x']
    return result

grid = [['70', 'x', '50', 'x'], ['x', '39', '46', 'x'], ['34', '60', 'x', '51'], ['x', 'x', 'x', '68']]
print(magic_square(grid))
