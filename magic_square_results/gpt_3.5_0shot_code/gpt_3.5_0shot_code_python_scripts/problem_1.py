
import itertools

def is_magic_square(grid):
    row_sums = [sum(row) for row in grid]
    col_sums = [sum(col) for col in zip(*grid)]
    diag_sum1 = sum(grid[i][i] for i in range(3))
    diag_sum2 = sum(grid[i][2-i] for i in range(3))
    
    return all(x == 107 for x in col_sums) and all(x == 103 for x in row_sums) and diag_sum1 == 124 and diag_sum2 == 124

def find_min_sum_magic_square():
    grid = [['35', 'x', '46'],
            ['x', 'x', 'x'],
            ['x', 'x', 'x']]
    
    possible_values = [i for i in range(29, 49)]
    min_sum = float('inf')
    min_grid = None
    
    for perm in itertools.permutations(possible_values, 6):
        grid[0][1] = str(perm[0])
        grid[0][2] = str(perm[1])
        grid[1][0] = str(perm[2])
        grid[1][1] = str(perm[3])
        grid[1][2] = str(perm[4])
        grid[2][0] = str(perm[5])
        
        if is_magic_square(grid):
            current_sum = sum(int(num) for row in grid for num in row if num != 'x')
            if current_sum < min_sum:
                min_sum = current_sum
                min_grid = [tuple([i, j, int(grid[i][j])] for i in range(3) for j in range(3) if grid[i][j] != 'x')]
    
    return min_grid

solution = find_min_sum_magic_square()
print(solution)
