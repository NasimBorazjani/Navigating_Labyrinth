
def magic_square(grid, constraints):
    def valid(grid, row, col, num):
        # Check the number doesn't exist in the same row or column
        for i in range(4):
            if grid[row][i] == num or grid[i][col] == num:
                return False

        # Check the number doesn't exist in the same 3x3 box
        start_row, start_col = row - row % 3, col - col % 3
        for i in range(3):
            for j in range(3):
                if grid[i + start_row][j + start_col] == num:
                    return False

        return True

    def solve(grid, row=0, col=0):
        if grid[row][col] == 'x':
            for num in range(30, 67):
                if valid(grid, row, col, num):
                    grid[row][col] = num
                    if solve(grid, (col + 1) % 4, (row + (col + 1) // 4) % 4):
                        return True
                    grid[row][col] = 'x'
            return False
        else:
            if (col + 1) % 4 == 0 and row == 3 or col == 3 and row == 1:
                if sum(grid[i][col] for i in range(4)) != constraints[col]:
                    return False
            if row == 3 and col == 3:
                if sum(grid[row][i] for i in range(4)) != constraints[3]:
                    return False
            if row == 1 and col == 3:
                if sum(grid[i][row] for i in range(4)) != constraints[1]:
                    return False
            if row == 2 and col == 0:
                if sum(grid[i][3 - i] for i in range(4)) != constraints[2]:
                    return False
            if row == 3 and col == 0:
                if sum(grid[3 - i][i] for i in range(4)) != constraints[0]:
                    return False
            return solve(grid, (col + 1) % 4, (row + (col + 1) // 4) % 4)

    if solve(grid):
        return [(i, j, grid[i][j]) for i in range(4) for j in range(4) if grid[i][j] != 'x']

grid = [['x', 'x', 'x', 'x'],
        ['40', '39', '32', '53'],
        ['46', 'x', '58', 'x'],
        ['x', 'x', '43', '51']]

constraints = [None, 199, 194, None]

print(magic_square(grid, constraints))
