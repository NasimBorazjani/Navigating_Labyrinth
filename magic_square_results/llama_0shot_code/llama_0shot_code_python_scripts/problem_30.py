
from itertools import permutations

def magic_square(grid, row_sums, col_sums, diag_sum):
    best_sum = float('inf')
    best_grid = None
    for perm in permutations(range(34, 79), 9):
        temp_grid = [[num if num != 'x' else 'x' for num in row] for row in grid]
        for i in range(9):
            for row in range(3):
                for col in range(3):
                    if temp_grid[row][col] == 'x':
                        temp_grid[row][col] = perm[i]
                        break
        if (sum(temp_grid[0]) == row_sums[0] and
            sum(temp_grid[1]) == row_sums[1] and
            sum(temp_grid[2]) == row_sums[2] and
            sum(temp_grid[i][0] for i in range(3)) == col_sums[0] and
            sum(temp_grid[i][1] for i in range(3)) == col_sums[1] and
            sum(temp_grid[i][2] for i in range(3)) == col_sums[2] and
            temp_grid[0][0] + temp_grid[1][1] + temp_grid[2][2] == diag_sum and
            temp_grid[0][2] + temp_grid[1][1] + temp_grid[2][0] == diag_sum):
            if sum(perm[0:9]) < best_sum:
                best_sum = sum(perm[0:9])
                best_grid = perm
    return [(i//3, i%3, val) for i, val in enumerate(best_grid)]

grid = [['x', 'x', '59'], ['x', 'x', 'x'], ['38', 'x', 'x']]
row_sums = [212, 172, 165]
col_sums = [172, 172, 165]
diag_sum = 165

print(magic_square(grid, row_sums, col_sums, diag_sum))
