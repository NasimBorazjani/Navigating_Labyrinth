
def solve_magic_square(grid, row_sums, col_sums, diagonal_sum, range_start, range_end):
    solutions = []

    def backtrack(row, col, values):
        if row == len(grid):
            if all(sum(grid[i][j] for i in range(len(grid))) == row_sums[i] for i in range(len(row_sums))) and \
               all(sum(grid[i][j] for j in range(len(grid[0]))) == col_sums[j] for j in range(len(col_sums))) and \
               sum(grid[i][i] for i in range(len(grid))) - grid[1][1] == diagonal_sum:
                solutions.append(values)
        else:
            for i in range(col if row == col else len(grid[0])):
                if grid[row][i] == 'x':
                    for value in range(range_start, range_end + 1):
                        if value not in values and value not in grid[row]:
                            grid[row][i] = value
                            backtrack(row + (0 if i + 1 == len(grid[0]) else 1), (0 if i + 1 == len(grid[0]) else col + 1), values + (row, i, value))
                            grid[row][i] = 'x'

    backtrack(0, 0, ())
    return solutions

grid = [['x', 'x', 'x', '67'], ['62', 'x', '32', '77'], ['66', 'x', '34', 'x'], ['x', 'x', '73', '35']]
row_sums = [None, 220, None]
col_sums = [None, 239, 192, None]
diagonal_sum = 199
range_start = 30
range_end = 86

solutions = solve_magic_square(grid, row_sums, col_sums, diagonal_sum, range_start, range_end)
print(solutions)
