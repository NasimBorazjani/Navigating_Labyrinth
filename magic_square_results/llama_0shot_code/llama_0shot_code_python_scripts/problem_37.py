
def solve_magic_square(grid):
    def backtrack(grid, row, col, num):
        if num == 0:
            return True
        if col == len(grid[0]):
            col = 0
            row += 1
        if row == len(grid):
            return False
        if grid[row][col] != 'x':
            return backtrack(grid, row, col + 1, num - grid[row][col])
        for i in range(1, 50):
            grid[row][col] = i
            if backtrack(grid, row, col + 1, num - i):
                return True
        grid[row][col] = 'x'
        return False

    backtrack(grid, 0, 0, 209)
    return [(row, col, grid[row][col]) for row in range(len(grid)) for col in range(len(grid[0])) if grid[row][col] != 'x']

grid = [['48', 'x', 'x'], ['x', 'x', 'x'], ['x', '49', 'x']]
result = solve_magic_square(grid)
print(result)
