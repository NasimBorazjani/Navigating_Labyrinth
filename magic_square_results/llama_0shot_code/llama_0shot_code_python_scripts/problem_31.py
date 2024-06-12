
from itertools import permutations

def magic_square(given, sums):
    min_sum = sum(sums)
    for perm in permutations(range(34, 79)):
        grid = [[perm[i] for i in row] for row in given]
        if (sum(grid[0][0], grid[0][1], grid[0][2]) == sums[0] and
            sum(grid[1][0], grid[1][1], grid[1][2]) == sums[1] and
            sum(grid[2][0], grid[2][1], grid[2][2]) == sums[2] and
            grid[0][0] + grid[1][1] + grid[2][2] == sums[3]):
            total_sum = sum(sum(row) for row in grid)
            if total_sum < min_sum:
                min_sum = total_sum
                best_grid = grid
    return [(i, j, val) for i, row in enumerate(best_grid) for j, val in enumerate(row) if val not in given[i]]

given = [['x', 'x', 'x'], ['x', '73', '47'], ['x', 'x', 'x']]
sums = [177, 180, 183, 310]
print(magic_square(given, sums))
