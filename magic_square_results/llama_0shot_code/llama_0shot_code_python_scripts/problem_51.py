
def solve_magic_square(grid):
    rows = [None, 72, 97, None]
    cols = [None, 102, 100, None]
    total = 46
    nums = list(range(9, 41))
    solution = []

    def is_valid(row, col, num):
        # Check row constraint
        if rows[row] is not None and rows[row] - num < 0:
            return False

        # Check column constraint
        if cols[col] is not None and cols[col] - num < 0:
            return False

        # Check diagonal constraint
        if row == col and total - num * 2 < 0:
            return False

        return True

    def backtrack(row=0, col=0):
        if row == len(grid):
            return True

        if col == len(grid[row]):
            col = 0
            row += 1

        if grid[row][col] != 'x':
            return backtrack(row, col + 1)

        for num in nums:
            if is_valid(row, col, num):
                grid[row][col] = num
                solution.append((row, col, num))

                if backtrack(row, col + 1):
                    return True

                solution.pop()
                grid[row][col] = 'x'

        return False

    backtrack()

    return solution

grid = [['x', 'x', '27', '9'], ['21', 'x', 'x', '15'], ['x', '16', '31', 'x'], ['11', 'x', '32', 'x']]
print(solve_magic_square(grid))
