
def solve_grid():
    grid = [['x', '57', 'x'], ['42', 'x', '72'], ['39', 'x', '73']]
    for i in range(3):
        for j in range(3):
            if grid[i][j] == 'x':
                for num in range(39, 87):
                    if is_valid(grid, i, j, num):
                        grid[i][j] = num
                        break
    return grid

def is_valid(grid, row, col, num):
    # Check the number in the row
    if row > 0 and grid[row-1][col] > num or row < 2 and grid[row+1][col] < num:
        return False
    # Check the number in the column
    if col > 0 and grid[row][col-1] > num or col < 2 and grid[row][col+1] < num:
        return False
    # Check the number in the diagonal
    if row > 0 and col > 0 and grid[row-1][col-1] > num or row < 2 and col < 2 and grid[row+1][col+1] < num:
        return False
    return True

print(solve_grid())
