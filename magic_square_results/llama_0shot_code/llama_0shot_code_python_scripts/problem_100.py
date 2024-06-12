
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
        if grid[row][col] == 'x':
            for num in range(30, 87):
                if is_valid(row, col, num):
                    grid[row][col] = str(num)
                    if solve(grid, (row + 1) % 4, col):
                        return True
                    grid[row][col] = 'x'
            return False
        else:
            return solve(grid, (row + 1) % 4, col)

    def get_solution(grid):
        result = []
        for i in range(4):
            for j in range(4):
                if grid[i][j] != 'x':
                    result.append((i, j, int(grid[i][j])))
        return result

    if not solve(grid, 0, 0):
        return None
    return get_solution(grid)

grid = [['32', '75', '36', 'x'], ['x', '83', 'x', 'x'], ['x', '77', '58', '44'], ['x', '60', 'x', 'x']]
print(solve_magic_square(grid))
