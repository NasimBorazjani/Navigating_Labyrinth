
import itertools

def is_magic_square(grid):
    # Check if the sums of rows, columns, and diagonal are correct
    row_sums = [sum(row) for row in grid]
    col_sums = [sum(col) for col in zip(*grid)]
    diag_sum1 = sum(grid[i][i] for i in range(3))
    diag_sum2 = sum(grid[i][2-i] for i in range(3))
    
    return all(row_sum == 134 for row_sum in row_sums) and all(col_sum == 143 for col_sum in col_sums) and diag_sum1 == 131 and diag_sum2 == 131

def find_min_sum(grid):
    # Find the minimum sum of all numbers in the grid
    min_sum = float('inf')
    for perm in itertools.permutations(range(28, 58), 5):
        new_grid = [row.copy() for row in grid]
        idx = 0
        for i in range(3):
            for j in range(3):
                if new_grid[i][j] == 'x':
                    new_grid[i][j] = perm[idx]
                    idx += 1
        if is_magic_square(new_grid):
            min_sum = min(min_sum, sum(sum(row) for row in new_grid))
    
    return min_sum

grid = [['x', '32', 'x'],
        ['38', 'x', 'x'],
        ['x', 'x', 'x']]

min_sum = find_min_sum(grid)
print("Minimum sum of all numbers in the grid:", min_sum)
