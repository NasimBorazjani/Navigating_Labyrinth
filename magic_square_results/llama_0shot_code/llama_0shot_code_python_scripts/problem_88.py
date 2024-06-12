
def solve_magic_square(grid, row_sums, col_sums, diag_sum):
    def is_valid(row, col, num):
        # Check row
        if row_sums[row] is not None and row_sums[row] - num < 0:
            return False
        # Check column
        if col_sums[col] is not None and col_sums[col] - num < 0:
            return False
        # Check diagonal
        if row == col and diag_sum - num < 0:
            return False
        return True

    def backtrack(row, col, sum_so_far):
        nonlocal best_sum, best_grid
        if sum_so_far > best_sum:
            return
        if row == len(grid):
            if col == len(grid[0]):
                if sum_so_far == best_sum:
                    best_grid = [row_sums[:], col_sums[:], diag_sum]
            return
        if grid[row][col] != 'x':
            backtrack(row + (col + 1) // len(grid), col + 1, sum_so_far + grid[row][col])
        else:
            for num in range(22, 69):
                if is_valid(row, col, num):
                    # Update row sum
                    if row_sums[row] is not None:
                        row_sums[row] -= num
                    # Update column sum
                    if col_sums[col] is not None:
                        col_sums[col] -= num
                    # Update diagonal sum
                    if row == col:
                        diag_sum -= num
                    # Recurse
                    backtrack(row + (col + 1) // len(grid), col + 1, sum_so_far + num)
                    # Undo updates
                    if row_sums[row] is not None:
                        row_sums[row] += num
                    if col_sums[col] is not None:
                        col_sums[col] += num
                    if row == col:
                        diag_sum += num

    best_sum = float('inf')
    best_grid = None
    row_sums = [None, 183, 202, None]
    col_sums = [None, 190, 154, None]
    diag_sum = 183
    backtrack(0, 0, 0)
    return [(i, j, grid[i][j]) for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j] != 'x']

grid = [['27', '48', 'x', 'x'], ['x', 'x', '63', 'x'], ['28', 'x', '33', '26'], ['x', 'x', 'x', '39']]
grid = [[int(cell) if cell.isdigit() else cell for cell in row] for row in grid]
print(solve_magic_square(grid, [None, 183, 202, None], [None, 190, 154, None], 183))
