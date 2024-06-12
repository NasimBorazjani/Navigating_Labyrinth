
def solve_magic_square():
    grid = [['46', '30', 'x', '49'],
            ['43', 'x', 'x', '53'],
            ['x', 'x', '37', 'x'],
            ['x', '34', '33', 'x']]

    def valid(num, row, col):
        # Check the number hasn't been used yet
        for i in range(4):
            for j in range(4):
                if grid[i][j] == num:
                    return False

        # Check the row constraint
        if row == 0 and sum([int(grid[0][j]) for j in range(4) if grid[0][j] != 'x']) + num != 173:
            return False
        if row == 1 and sum([int(grid[1][j]) for j in range(4) if grid[1][j] != 'x']) + num != 194:
            return False

        # Check the column constraint
        if col == 1 and sum([int(grid[i][1]) for i in range(4) if grid[i][1] != 'x']) + num != 154:
            return False
        if col == 2 and sum([int(grid[i][2]) for i in range(4) if grid[i][2] != 'x']) + num != 157:
            return False

        # Check the diagonal constraint
        if row == 3 and col == 0 and sum([int(grid[i][3 - i]) for i in range(4) if grid[i][3 - i] != 'x']) + num != 208:
            return False

        return True

    def backtrack(row, col):
        if row == 4:  # All cells are filled
            return True
        if grid[row][col] != 'x':  # This cell is already filled
            return backtrack(row + (col + 1) // 4, (col + 1) % 4)

        for num in map(str, range(30, 67)):  # Try the next number
            if valid(num, row, col):
                grid[row][col] = num
                if backtrack(row + (col + 1) // 4, (col + 1) % 4):
                    return True
        grid[row][col] = 'x'  # Backtrack
        return False

    backtrack(0, 0)

    # Check the sums
    if sum([int(grid[0][j]) for j in range(4) if grid[0][j] != 'x']) != 173 or \
       sum([int(grid[1][j]) for j in range(4) if grid[1][j] != 'x']) != 194 or \
       sum([int(grid[i][1]) for i in range(4) if grid[i][1] != 'x']) != 154 or \
       sum([int(grid[i][2]) for i in range(4) if grid[i][2] != 'x']) != 157 or \
       sum([int(grid[i][3 - i]) for i in range(4) if grid[i][3 - i] != 'x']) != 208:
        return "No solution found"

    return [(row, col, int(num)) for row in range(4) for col in range(4) for num in (grid[row][col],) if num != 'x']

print(solve_magic_square())
