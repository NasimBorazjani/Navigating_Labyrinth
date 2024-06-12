
def solve_magic_square(grid, row_sums, col_sums, diag_sum):
    def is_valid(num, row, col):
        # Check the number hasn't been used yet in the row or column
        if num in rows[row] or num in cols[col]:
            return False
        return True

    def backtrack(row, col):
        if row == len(grid):
            # Check the sum of the diagonal
            if sum(grid[i][i] for i in range(len(grid))) != diag_sum:
                return False
            return grid

        if col == len(grid[0]):
            return backtrack(row + 1, 0)

        if grid[row][col] == 'x':
            for num in range(35, 62):
                if is_valid(num, row, col):
                    rows[row].add(num)
                    cols[col].add(num)
                    grid[row][col] = num

                    result = backtrack(row, col + 1)
                    if result:
                        return result

                    grid[row][col] = 'x'
                    rows[row].remove(num)
                    cols[col].remove(num)

        else:
            result = backtrack(row, col + 1)
            if result:
                return result

    rows = [set() for _ in range(len(grid))]
    cols = [set() for _ in range(len(grid[0]))]

    for row, sums in enumerate(row_sums):
        if sums is not None:
            for col, num in enumerate(grid[row]):
                if num != 'x':
                    rows[row].add(num)
                    cols[col].add(num)

    return backtrack(0, 0)

grid = [['x', 'x', 'x', 'x'],
        ['x', '37', 'x', '41'],
        ['48', 'x', 'x', 'x'],
        ['49', 'x', '46', '38']]

row_sums = [None, 180, None, None]
col_sums = [None, 151, 189, None]
diag_sum = 184

result = solve_magic_square(grid, row_sums, col_sums, diag_sum)

output = [(row, col, num) for row, row_nums in enumerate(result) for col, num in enumerate(row_nums) if num != 'x']
print(output)
