
import numpy as np

def solve_magic_square(grid, row_sums, col_sums, diag_sum, used, total):
    # Check if all cells are filled
    if np.all(grid != 'x'):
        # Check if the sums of the rows, columns, and diagonal are correct
        if all(np.sum(grid, axis=1)[i] == row_sums[i] for i in range(4) if row_sums[i] is not None) and \
           all(np.sum(grid, axis=0)[i] == col_sums[i] for i in range(4) if col_sums[i] is not None) and \
           np.trace(grid[::-1]) == diag_sum and \
           np.sum(grid) == total:
            return [(i, j, grid[i, j]) for i in range(4) for j in range(4) if isinstance(grid[i, j], int)]
    else:
        # Find the first 'x' in the grid
        x = np.argwhere(grid == 'x')[0]
        # Try all possible values for this cell
        for v in range(36, 93):
            if v not in used and \
               (row_sums[x[0]] is None or np.sum(grid[x[0], :]) + v <= row_sums[x[0]]) and \
               (col_sums[x[1]] is None or np.sum(grid[:, x[1]]) + v <= col_sums[x[1]]) and \
               (x[0] + x[1] != 3 or np.trace(grid[::-1]) + v <= diag_sum) and \
               np.sum(grid) + v <= total:
                # Assign the value to the cell
                grid[x[0], x[1]] = v
                used.add(v)
                # Recursively solve the rest of the grid
                solution = solve_magic_square(grid, row_sums, col_sums, diag_sum, used, total)
                if solution is not None:
                    return solution
                # If no solution was found, backtrack
                grid[x[0], x[1]] = 'x'
                used.remove(v)

grid = np.array([['x', 69, 'x', 'x'],
                 ['x', 62, 'x', 'x'],
                 ['x', 82, 40, 'x'],
                 ['x', 87, 78, 80]], dtype=object)
row_sums = [None, 214, 240, None]
col_sums = [None, 300, 191, None]
diag_sum = 249
used = set(grid[grid != 'x'])
total = sum(row_sums[i] for i in range(4) if row_sums[i] is not None) + sum(col_sums[i] for i in range(4) if col_sums[i] is not None) - diag_sum
solution = solve_magic_square(grid, row_sums, col_sums, diag_sum, used, total)
print(solution)
