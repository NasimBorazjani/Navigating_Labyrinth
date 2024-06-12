
from itertools import permutations

def magic_square(grid, row_sums, col_sums, diag_sum):
    # Generate all permutations of the numbers in the given range
    perms = permutations(range(26, 66))
    result = []
    
    for perm in perms:
        temp_grid = grid.copy()   # Create a copy of the grid to fill
        for i in range(9):
            if temp_grid[i//3][i%3] == 'x':
                temp_grid[i//3][i%3] = perm[i]   # Fill the 'x' position with the current number from the permutation
        
        # Check if the sums of the row, column, and diagonal are correct
        if (sum(temp_grid[0]) == row_sums[0] and
            sum(temp_grid[1]) == row_sums[1] and
            sum(temp_grid[2]) == row_sums[2] and
            sum(temp_grid[i][i] for i in range(3)) == diag_sum):
            for i in range(3):
                for j in range(3):
                    if temp_grid[i][j] == 'x':
                        result.append((i, j, perm[i*3+j]))
    return result

grid = [['x', 'x', 'x'], ['x', 'x', 'x'], ['x', '32', 'x']]
row_sums = [135, 150, 119]
col_sums = [150, 135, 119]
diag_sum = 119

print(magic_square(grid, row_sums, col_sums, diag_sum))
