
def solve_magic_square(grid):
    # List of all numbers in the range 9 to 40
    numbers = list(range(9, 41))

    # Function to check if a number can be placed at a position
    def is_valid(row, col, num):
        # Check the number isn't already in the grid
        for i in range(4):
            for j in range(4):
                if grid[i][j] == num:
                    return False

        # Check the number satisfies the row and column constraints
        for i in range(4):
            if grid[row][i] == 'x' or grid[i][col] == 'x':
                continue
            if grid[row][i] + num > 116 or grid[i][col] + num > 78:
                return False

        # Check the number satisfies the diagonal constraint
        if row + col == 3 and grid[0][3] + num > 31:
            return False

        return True

    # Function to solve the grid
    def solve(row=0, col=0):
        if row == 4:
            return True
        if col == 4:
            return solve(row + 1, 0)

        if grid[row][col] != 'x':
            return solve(row, col + 1)

        for num in numbers:
            if is_valid(row, col, num):
                grid[row][col] = num
                if solve(row, col + 1):
                    return True
                grid[row][col] = 'x'

        return False

    # Function to get the solution
    def get_solution():
        solve()
        result = []
        for i in range(4):
            for j in range(4):
                if grid[i][j] != 'x':
                    result.append((i, j, grid[i][j]))
        return result

    return get_solution()

grid = [['x', 'x', 22, 23],
        ['x', 'x', 15, 25],
        [31, 'x', 'x', 'x'],
        [12, 36, 'x', 13]]

print(solve_magic_square(grid))
