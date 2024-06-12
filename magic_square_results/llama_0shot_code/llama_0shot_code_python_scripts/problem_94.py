
def solve_magic_square(grid):
    def is_valid(row, col, num):
        # Check the number doesn't exist in the same row, column, or square
        for i in range(4):
            if grid[row][i] == str(num) or grid[i][col] == str(num):
                return False
            x, y = row - row % 2 + i // 2, col - col % 2 + i % 2
            if grid[x][y] == str(num):
                return False
        return True

    def solve(grid, row, col):
        if grid[row][col] != 'x':
            if col + 1 < 4:
                return solve(grid, row, col + 1)
            elif row + 1 < 4:
                return solve(grid, row + 1, 0)
            else:
                return [tuple(map(int, row)) for row in grid]
        for num in range(41, 93):
            if is_valid(row, col, num):
                grid[row][col] = str(num)
                if col + 1 < 4:
                    result = solve(grid, row, col + 1)
                elif row + 1 < 4:
                    result = solve(grid, row + 1, 0)
                else:
                    result = [tuple(map(int, row)) for row in grid]
                if result:
                    return result
                grid[row][col] = 'x'
        return None

    return solve(grid, 0, 0)

grid = [['48', 'x', 'x', 'x'],
        ['54', 'x', 'x', 'x'],
        ['x', '64', '44', '83'],
        ['82', '68', '51', 'x']]

print(solve_magic_square(grid))
